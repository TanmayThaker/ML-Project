from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger
from pathlib import Path

STAGE_NAME  = "Model Training Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()


if __name__=="__main__":
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started. <<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} completed! <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e