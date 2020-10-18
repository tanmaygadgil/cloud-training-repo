from flask_restful import Api
from app import flaskAppInstance
from .predict import HousePredictor
from .train import HouseTrainer

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(PlmAPI,"/predict/")
restServerInstance.add_resource(PlmAPI,"/train/<string:path>")