import joblib
import numpy as np
import os

try:
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError as e:
    raise FileNotFoundError(f"Model files not found: {e}. Make sure diabetes_model.pkl and scaler.pkl are in the app directory.")


def predict_diabetes(data):

    data = np.array(data).reshape(1, -1)

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(scaled)[0][1]

    return prediction, probability