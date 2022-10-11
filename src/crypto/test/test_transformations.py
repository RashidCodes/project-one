import yaml
from crypto.elt.transform import Transform
from database.postgres import PostgresDB


class TestTransformations:

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



    def test_staging_coin_price_history(self):

        """ Use the Transform class to transform the coin price history data for staging """
        
        results = Transform("staging_coin_price_history", engine=self.target_engine, models_path=self.path_transform_model)
        assert results.run() == True



    def test_serving_coin_price_history(self):

        """ Use the Transform class to transform the coin price history data for staging """
        
        results = Transform("serving_coin_price_history", engine=self.target_engine, models_path=self.path_transform_model)
        assert results.run() == True


    
    def test_staging_coins_history(self):

        """ Use the Transform class to transform the coin price history data for staging """
        
        results = Transform("staging_coins_history", engine=self.target_engine, models_path=self.path_transform_model)
        assert results.run() == True



    def test_serving_coins_history(self):

        """ Use the Transform class to transform the coin price history data for serving """
        
        results = Transform("serving_coins_history", engine=self.target_engine, models_path=self.path_transform_model)
        assert results.run() == True