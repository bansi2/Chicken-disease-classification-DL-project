from src.CNNClassifier.config.configuration import ConfigurationManager
from src.CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

STAGE_NAME = "PREPARE BASE MODEL"

class PrepareBaseModelTrainingPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
            
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModel()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e