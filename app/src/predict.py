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

MODEL_PATH = os.path.join(os.getcwd() , 'models/xgb_regressor_snapshot.bin')

class HousePredictor(Resource):
    def post(self):
        input_data = request.get_json(force=True)
        print(os.getcwd())
        xgb_model = load_model()
        input_pd = pd.DataFrame(columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT'])

    def load_model(self):
        with open(MODEL_PATH, 'rb') as file:
            xgb_model = pickle.load(file)

        return xgb_model
    
    def set_input_pd(self):
        