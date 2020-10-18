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

class HouseTrainer(Resource):
    def post(self, path):
        input_data = request.get_json(force=True)
        print(os.getcwd())