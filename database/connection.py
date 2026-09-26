from sqlalchemy import create_engine


DATABASE_URL = (
    "mysql+pymysql://root:hasnain0786%40@localhost:3306/house_price_db"
)


engine = create_engine(
    DATABASE_URL
)


def get_connection():
    return engine.connect()


if __name__ == "__main__":

    try:
        connection = get_connection()

        print("MySQL connection successful! ✅")

        connection.close()

    except Exception as e:

        print("MySQL connection failed! ❌")
        print("Error:", e)