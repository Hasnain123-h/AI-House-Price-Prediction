   
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sqlalchemy import text

from src.predict import predict_ann_price
from database.crud import save_prediction
from database.connection import get_connection


app = FastAPI(
    title="House Price Prediction API",
    description="API for California House Price Prediction",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running!"
    }


class HouseData(BaseModel):

    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str


@app.post("/predict")
def predict_house_price(data: HouseData):

    input_data = pd.DataFrame({
        "longitude": [data.longitude],
        "latitude": [data.latitude],
        "housing_median_age": [data.housing_median_age],
        "total_rooms": [data.total_rooms],
        "total_bedrooms": [data.total_bedrooms],
        "population": [data.population],
        "households": [data.households],
        "median_income": [data.median_income],
        "ocean_proximity": [data.ocean_proximity]
    })

    predicted_price = predict_ann_price(
        input_data
    )

    save_prediction(
        data.model_dump(),
        predicted_price
    )

    return {
        "predicted_house_price": predicted_price
    }


@app.get("/predictions")
def get_predictions():

    connection = get_connection()

    query = text("""
        SELECT *
        FROM house_predictions
        ORDER BY id DESC
    """)

    result = connection.execute(query)

    predictions = [
        dict(row._mapping)
        for row in result
    ]

    connection.close()

    return {
        "predictions": predictions
    }    