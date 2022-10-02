from matplotlib.pyplot import show
from crypto.elt.extract import Extract
from crypto.elt.load import Load

class ExtractLoad():

    def __init__(self, source_engine, target_engine, table_name, path, path_extract_log, chunksize:int=1000):
        self.source_engine = source_engine
        self.target_engine = target_engine
        self.table_name = table_name
        self.path = path 
        self.path_extract_log = path_extract_log
        self.chunksize = chunksize

    def run(self):
        
        #Extract dataframe
        df = Extract.extract_from_api(table_name=self.table_name, path=self.path, path_extract_log=self.path_extract_log)

        #Load table  
        if len(df) > 0 :
            if Extract.is_incremental(table=self.table_name, path=self.path):
                key_columns = Load.get_key_columns(table=self.table_name, path=self.path)
                Load.upsert_to_database(df=df, table_name=self.table_name, key_columns=key_columns, engine=self.target_engine, chunksize=self.chunksize )
                # print(f"{self.table_name} successfully loaded incrementally")
            else:
                Load.overwrite_to_database(df,table_name=self.table_name, engine=self.target_engine)
                # print(f"{self.table_name} fully loaded")