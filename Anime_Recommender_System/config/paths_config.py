import os 

##################### Data Ingestion ################################

RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"

GOOGLE_KEY_PATH = r"C:\Users\user\Desktop\brainwave-basket\Anime_Recommender_System\recom_key.json"