import yaml
from crypto.elt.extract import Extract
from crypto.pipeline.extract_load_pipeline import ExtractLoad
from database.postgres import PostgresDB


class TestExtractsAndLoads:


    def setup_class(self):
        
        config_path = "crypto/config.yaml"

        # get yaml config 
        with open(config_path) as stream:
            self.config = yaml.safe_load(stream)

        # set up the target engine 
        self.target_engine = PostgresDB.create_pg_engine(db_target="target")

        # location of extraction models 
        self.path_extract_model = self.config["extract"]["model_path"]

        # location of transformation models 
        self.path_transform_model = self.config["transform"]["model_path"]

        # location of logs
        self.path_extract_log = self.config["extract"]["log_path"]
            


    def test_coin_price_history_extraction(self):

        """ Use the extract_from_api method to extract coin price history"""

        table_name = 'coin_price_history'


        df = Extract.extract_from_api(table_name=table_name, path=self.path_extract_model, path_extract_log=self.path_extract_log)
        assert df.shape[0] > 0 



    def test_coin_history_extraction(self):

        """ Use the extract_from_api method to extract coin history"""

        table_name = 'coins_history'

        df = Extract.extract_from_api(table_name=table_name, path=self.path_extract_model, path_extract_log=self.path_extract_log)
        assert df.shape[0] > 0 



    def test_coin_price_history_load(self):

        """ Load coin price history data using the Load method """

        table_name = 'coin_price_history' # model name

        extract_load = ExtractLoad(

            target_engine=self.target_engine,
            table_name=table_name,
            path=self.path_extract_model,
            path_extract_log=self.path_extract_log
        )

        assert extract_load.run() == True



    def test_coin_history_load(self):

        """ Load coin price history data using the Load method """

        table_name = 'coins_history' # model name

        extract_load = ExtractLoad(
            
            target_engine=self.target_engine,
            table_name=table_name,
            path=self.path_extract_model,
            path_extract_log=self.path_extract_log
        )

        assert extract_load.run() == True






