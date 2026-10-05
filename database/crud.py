from sqlalchemy import text

from database.connection import get_connection
def save_prediction(data, predicted_price):
    connection = get_connection()

    query = text("""
        INSERT INTO house_predictions (
            longitude,
            latitude,
            housing_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            ocean_proximity,
            predicted_price
        )
        VALUES (
            :longitude,
            :latitude,
            :housing_median_age,
            :total_rooms,
            :total_bedrooms,
            :population,
            :households,
            :median_income,
            :ocean_proximity,
            :predicted_price
        )
    """)

    connection.execute(
        query,
        {
            "longitude": data["longitude"],
            "latitude": data["latitude"],
            "housing_median_age": data["housing_median_age"],
            "total_rooms": data["total_rooms"],
            "total_bedrooms": data["total_bedrooms"],
            "population": data["population"],
            "households": data["households"],
            "median_income": data["median_income"],
            "ocean_proximity": data["ocean_proximity"],
            "predicted_price": predicted_price
        }
    )

    connection.commit()
    connection.close()