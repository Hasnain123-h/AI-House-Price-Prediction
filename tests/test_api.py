from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_predict_api():

    data = {
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41,
        "total_rooms": 880,
        "total_bedrooms": 129,
        "population": 322,
        "households": 126,
        "median_income": 8.3252,
        "ocean_proximity": "NEAR BAY"
    }

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 200

    result = response.json()

    assert "predicted_house_price" in result

    assert result["predicted_house_price"] > 0