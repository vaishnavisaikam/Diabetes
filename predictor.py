import joblib
import numpy as np

model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_diabetes(data):

    data = np.array(data).reshape(1, -1)

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(scaled)[0][1]

    return prediction, probability