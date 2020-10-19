import os
import pickle
import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
# from sklearn import metrics
# from xgboost import XGBRegressor
from flask import request
from flask_restful import Resource


MODEL_PATH = os.path.join(os.getcwd(), 'models/xgb_regressor_snapshot.bin')
FEATURE_COLS = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
                'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                'PTRATIO', 'B', 'LSTAT']

class HousePredictor(Resource):
    """
    Class to act as Predictor resource
    """

    def load_model(self):
        """
        Module to load in the xgb model from local or bucket
        """
        with open(MODEL_PATH, 'rb') as file:
            xgb_model = pickle.load(file)

        return xgb_model

    def post(self):
        """
        Main function defining the functionality of the 
        post request
        """
        input_data = request.get_json(force=True)

        print(os.getcwd())
        xgb_model = self.load_model()
        print(">>model Loaded")
        print(input_data)
        input_data = json_normalize(input_data)
        print(">>json Normalized")
        input_pd = input_data[FEATURE_COLS]
        print(">>json input data prepped")
        print(input_pd)
        prediction = float(xgb_model.predict(input_pd)[0])
        print(">> prediction: ", prediction)
        return {'PRICE': prediction}
