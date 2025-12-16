from src.CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CNNClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.CNNClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from src.CNNClassifier import logger

STAGE_NAME = "STAGE_01_DATA_INGESTION"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "STAGE_02_PREPARE_BASE_MODEL"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "STAGE_03_Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "STAGE_04_Evaluation"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

