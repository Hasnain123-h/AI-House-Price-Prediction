from pathlib import Path

import joblib
import pandas as pd
from tensorflow import keras
from src.feature_engineering import prepare_input
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = (BASE_DIR/ "models"/ "ann_house_price_model.keras")
SCALER_PATH = (BASE_DIR/ "models"/ "ann_scaler.pkl")
FEATURES_PATH = (BASE_DIR/ "data"/ "processed"/ "X_train.csv")
def predict_ann_price(input_data):
    model = keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    X_train = pd.read_csv(FEATURES_PATH)
    feature_columns = X_train.columns.tolist()
    prepared_input = prepare_input(
        input_data,
        feature_columns
    )
    input_scaled = scaler.transform(
        prepared_input
    )
    prediction = model.predict(
        input_scaled,
        verbose=0
    )
    return float(prediction.flatten()[0])

if __name__ == "__main__":

    sample = pd.DataFrame({
        "longitude": [-122.23],
        "latitude": [37.88],
        "housing_median_age": [41],
        "total_rooms": [880],
        "total_bedrooms": [129],
        "population": [322],
        "households": [126],
        "median_income": [8.3252],
        "ocean_proximity": ["NEAR BAY"]
    })

    predicted_price = predict_ann_price(sample)
    print(
        "Predicted House Price:",
        predicted_price
    )


