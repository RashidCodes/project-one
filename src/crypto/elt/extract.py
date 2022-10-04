import pandas as pd
import jinja2 as j2 
import logging 
import os 
import datetime as dt 
from sqlalchemy import false
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

class Extract(): 

    @staticmethod
    def coins():
        try:
            df = pd.DataFrame(cg.get_coins_list(), columns=['id','name','symbol'])
            df['ingestion_date'] = pd.to_datetime("today").date().strftime("%d-%m-%Y")

            return df
        except:
            return False
    

    @staticmethod
    def trending():
        li=[]
        try:
            trend = cg.get_search_trending()
            for item in trend['coins']:
                li.append(item['item'])
            df = pd.DataFrame(li)
            df = df.drop(['coin_id','name','symbol','thumb','small','large','slug','price_btc'],axis=1)
            df['ingestion_date'] = pd.to_datetime("today").date().strftime("%d-%m-%Y")

            return df
        except:
            return False

    @staticmethod
    def coins_history(number_of_days):
        try:
            list_of_coins= ['bitcoin','litecoin','ethereum','solana' ,'umee','terra-luna','evmos','dejitaru-tsuka','reserve-rights-token','insights-network']
            list_his=[]
            start_date = pd.to_datetime("today") - pd.Timedelta(number_of_days, unit='D')
            for coin in list_of_coins:
                day = start_date
                while day.date() <= (pd.to_datetime("today").date()):
                    data = cg.get_coin_history_by_id(id=coin,date=day.date().strftime("%d-%m-%Y"), localization='false')
                    data['price_date']= day.date().strftime("%d-%m-%Y")
                    list_his.append(data)
                    day = day + pd.Timedelta(1, unit='D')
            
            df = pd.DataFrame(list_his)
            df['id_date']= df['id'].astype(str)+'_'+df['price_date'].astype(str)
            df=df[['id_date','id','symbol','name','market_data','price_date']]
            df['current_price'] = pd.json_normalize(df['market_data'])['current_price.usd']
            df['market_cap'] = pd.json_normalize(df['market_data'])['market_cap.usd']
            df = df.drop(['market_data','symbol','name'], axis = 1)
            df['ingestion_date'] = pd.to_datetime("today").date().strftime("%d-%m-%Y")
            
            return df
        except:
            return False

    @staticmethod
    def get_incremental_value(table_name, path="extract_log"):
        df = pd.read_csv(f"{path}/{table_name}.csv")
        return df[df["log_date"] == df["log_date"].max()]["incremental_value"].values[0]

    @staticmethod
    def is_incremental(table:str, path:str)->bool:
        # read sql contents into a variable 
        with open(f"{path}/{table}.sql") as f: 
            raw_sql = f.read()
        try: 
            config = j2.Template(raw_sql).make_module().config 
            return config["extract_type"].lower() == "incremental"
        except:
            return False

    @staticmethod
    def upsert_incremental_log(log_path, table_name, incremental_value)->bool:
        if f"{table_name}.csv" in os.listdir(log_path):
            df_existing_incremental_log = pd.read_csv(f"{log_path}/{table_name}.csv")
            df_incremental_log = pd.DataFrame(data={
                "log_date": [dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")], 
                "incremental_value": [incremental_value]
            })
            df_updated_incremental_log = pd.concat([df_existing_incremental_log,df_incremental_log])
            df_updated_incremental_log.to_csv(f"{log_path}/{table_name}.csv", index=False)
        else: 
            df_incremental_log = pd.DataFrame(data={
                "log_date": [dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")], 
                "incremental_value": [incremental_value]
            })
            df_incremental_log.to_csv(f"{log_path}/{table_name}.csv", index=False)
        return True 

    @staticmethod
    def extract_from_api(table_name, path, path_extract_log):

        logging.info(f"Extracting table: {table_name}")
        if f"{table_name}.sql" in os.listdir(path):
            # read sql contents into a variable 
            with open(f"{path}/{table_name}.sql") as f: 
                raw_sql = f.read()
            # get config 
            config = j2.Template(raw_sql).make_module().config 

            if Extract.is_incremental(table=table_name, path=path):
                if not os.path.exists(path_extract_log): 
                    os.mkdir(path_extract_log)
                if f"{table_name}.csv" in os.listdir(path_extract_log):
                        # get incremental value and perform incremental extract 
                    current_max_incremental_value = Extract.get_incremental_value(table_name, path=path_extract_log)


                if table_name == 'coins_history':
                    df = Extract.coins_history(1)
                
                if len(df) > 0: 
                    max_incremental_value = df[config["incremental_column"]].max()
                else: 
                    max_incremental_value = current_max_incremental_value
                
                Extract.upsert_incremental_log(log_path=path_extract_log, table_name=table_name, incremental_value=max_incremental_value)
                logging.info(f"Successfully extracted table: {table_name}, rows extracted: {len(df)}")

                return df

            else:      
                if table_name == 'coins':
                    df = Extract.coins()
                elif table_name == 'trending':
                    df = Extract.trending()
                elif table_name == 'coins_history':
                    df = Extract.coins_history(8)    
                    
                logging.info(f"Successfully extracted table: {table_name}, rows extracted: {len(df)}")

                return df
        else:
            logging.error(f"Could not find table: {table_name}")