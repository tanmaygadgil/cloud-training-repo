from flask_restful import Api
from app import flaskAppInstance
from .predict import HousePredictor
from .train import HouseTrainer

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(HousePredictor,"/predict")
restServerInstance.add_resource(HouseTrainer,"/train")