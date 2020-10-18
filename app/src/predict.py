import pandas as pd
import numpy as np
from sklearn import metrics
import os
import pickle
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from flask import Flask
from flask import json
from flask import request
from flask import jsonify
from flask_restful import Resource
from pandas.io.json import json_normalize

MODEL_PATH = os.path.join(os.getcwd() , 'models/xgb_regressor_snapshot.bin')
FEATURE_COLS = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 
                'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                'PTRATIO', 'B', 'LSTAT']

class HousePredictor(Resource):
    def load_model(self):
        with open(MODEL_PATH, 'rb') as file:
            xgb_model = pickle.load(file)

        return xgb_model

    def post(self):
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

    
