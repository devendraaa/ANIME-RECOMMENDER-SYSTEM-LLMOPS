from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import groq_api_key, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("initializing Recommendation Pipeline")

            Vector_build =VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = Vector_build.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever, groq_api_key, MODEL_NAME)

            logger.info("Pipeline initialize successfull...")

        except Exception as e:
            logger.error(f"Failed to Initialize Pipeline {str(e)}")
            raise CustomException("error during pipeline iniatialization", e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"received a query {query}")

            recommendation = self.recommender.get_recommendation(query)
            logger.info("Recommendation generate successfully..")
            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to get recommendations {str(e)}")
            raise CustomException("error during get recommendations", e)
