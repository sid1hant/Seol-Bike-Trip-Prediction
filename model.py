import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
#from xgboost import XGBRegressor

# Captures the path of current folder
curr_path = os.path.dirname(os.path.realpath(__file__))


feat_cols = ['Distance', 'Haversine', 'Pmonth', 'Pday', 'Phour', 'Pmin', 'PDweek',
       'Dmonth', 'Dday', 'Dhour', 'Dmin', 'DDweek', 'Temp', 'Precip', 'Wind',
       'Humid', 'Solar', 'Snow', 'GroundTemp', 'Dust']

model= joblib.load(curr_path + "/model1.joblib")


print(model)
def predict_duration(attributes: list):
    """ Returns Bike Trip Duration value"""

    pred = model.predict([attributes])
    print("Duration predicted")

    return int(pred)