
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 California House Price Prediction")

st.write(
    "Enter house details to predict the estimated house price."
)

st.subheader("Enter House Details")

st.sidebar.header("🏠 House Details")


longitude = st.sidebar.number_input(
    "Longitude",
    value=-122.23
)

latitude = st.sidebar.number_input(
    "Latitude",
    value=37.88
)

housing_median_age = st.sidebar.number_input(
    "Housing Median Age",
    min_value=1,
    value=41
)

total_rooms = st.sidebar.number_input(
    "Total Rooms",
    min_value=1,
    value=880
)

total_bedrooms = st.sidebar.number_input(
    "Total Bedrooms",
    min_value=1,
    value=129
)

population = st.sidebar.number_input(
    "Population",
    min_value=1,
    value=322
)

households = st.sidebar.number_input(
    "Households",
    min_value=1,
    value=126
)

median_income = st.sidebar.number_input(
    "Median Income",
    min_value=0.0,
    value=8.3252
)

ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    [
        "NEAR BAY",
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "ISLAND"
    ]
)



# Main information
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model",
        "ANN"
    )

with col2:
    st.metric(
        "Problem",
        "Regression"
    )

with col3:
    st.metric(
        "Target",
        "House Value"
    )


if st.button("Predict House Price"):

    data = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            predicted_price = result[
                "predicted_house_price"
            ]

            st.success(
                "House price predicted successfully!"
            )

            st.metric(
                "Predicted House Price",
                f"${predicted_price:,.2f}"
            )

        else:

            st.error(
                f"Prediction failed. "
                f"Status code: {response.status_code}"
            )

    except Exception as e:

        st.error(
            f"API connection error: {e}"
        )

st.divider()

st.subheader("📊 Prediction History")


try:

    response = requests.get(
        "http://127.0.0.1:8000/predictions"
    )

    if response.status_code == 200:

        result = response.json()

        predictions = result["predictions"]

        if predictions:

            df_history = pd.DataFrame(
                predictions
            )

            st.dataframe(
                df_history,
                # use_container_width=True
                width="stretch"
            )

        else:

            st.info(
                "No prediction history available."
            )

    else:

        st.error(
            "Could not fetch prediction history."
        )

except Exception as e:

    st.error(
        f"API connection error: {e}"
    )
    
    

st.divider()

st.subheader("🤖 AI Assistant")

question = st.text_input(
    "Ask a question about the House Price Prediction project"
)

if st.button("Ask AI"):

    if question.strip():

        try:
            from rag.retriever import get_relevant_documents
            from rag.generator import generate_answer

            documents = get_relevant_documents(
                question,
                n_results=2
            )

            answer = generate_answer(
                question,
                documents
            )

            st.write("### AI Answer")
            st.write(answer)

        except Exception as e:

            st.error(f"RAG error: {e}")

    else:

        st.warning("Please enter a question.")
        
        
        
        
        
            




