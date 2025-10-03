from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("starting to build pipeline")

        loader = AnimeDataLoader("D:/Anime Recommend/data/anime_with_synopsis.csv" , "D:/Anime Recommend/data/anime_Update_synopsis.csv")
        processed_csv = loader.load_and_process()

        logger.info("data load and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectors()

        logger.info("vector store build scuessfully:")

        logger.info("pipeline build successfully...")

    except Exception as e:
        logger.error(f"Failed to execute building pipeline {str(e)}")
        raise CustomException("error during pipeline initialization", e)
    
if __name__=='__main__':
    main()