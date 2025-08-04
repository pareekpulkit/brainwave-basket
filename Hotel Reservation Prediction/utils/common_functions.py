import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml 

logger = get_logger(__name__)

def set_enivron_gcp_key(key_path):
    try:
        logger.info('Loading GCP key') 
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
        return True 
    except Exception as e:
        logger.error("Issue loading key")
        raise CustomException("Issue loading key" , e)
    



def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"FIle is not in the given path")
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Succesfully read the YAML file")
            return config 
    except Exception as e:
        logger.error("Error while reading YAML file")
        raise CustomException("Failed to read YAML file" , e)
    
def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Fail to load data", e)