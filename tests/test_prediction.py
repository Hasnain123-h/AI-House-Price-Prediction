import pandas as pd

from src.predict import predict_ann_price


def test_house_price_prediction():

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

    predicted_price = predict_ann_price(
        sample
    )

    assert predicted_price > 0