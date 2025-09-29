import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:    
    def __init__(self,config):
        self.config =config['data_ingestion']
        self.bucket_name = self.config['bucket_name']
        self.bucket_file_name = self.config['bucket_file_name']
        self.train_ratio = self.config['train_ratio']

        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info(f"Data Ingestion started with {self.bucket_name} and file {self.bucket_file_name}")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.bucket_file_name)   #filename
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Downloaded {self.bucket_file_name} from GCP bucket {self.bucket_name} to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error(f"Error downloading file from GCP: {e}")
            raise CustomException("Failed to download file from GCP", e)

    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data=pd.read_csv(RAW_FILE_PATH)
            train_data,test_data=train_test_split(data,test_size=1-self.train_ratio,random_state=42)
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)
            logger.info(f"Data split into train and test sets with ratio {self.train_ratio} and saved to {TRAIN_FILE_PATH} and {TEST_FILE_PATH}")

        except Exception as e:
            logger.error(f"Error during data splitting: {e}")
            raise CustomException("Failed to split data", e)
        
    def run(self):
        try:
            logger.info("Data Ingestion process started")
            self.download_csv_from_gcp()    
            self.split_data()
            logger.info("Data Ingestion process completed successfully")
        except Exception as e:
            logger.error(f"Data Ingestion process failed: {e}")
            raise CustomException("Data Ingestion process failed", e)
        finally:
            logger.info("Data Ingestion process ended")

if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    data_ingestion = DataIngestion(config)
    data_ingestion.run()