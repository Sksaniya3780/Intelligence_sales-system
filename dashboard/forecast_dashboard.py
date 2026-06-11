import streamlit as st
import pandas as pd

from model.predict import predict_sales


def show_forecast_dashboard():

    st.title("Sales Forecast Dashboard")

    st.write("Forecast future sales using trained ML model")

    sales = st.number_input(
        "Current Sales",
        min_value=0.0,
        value=1000.0
    )

    inventory = st.number_input(
        "Inventory Level",
        min_value=0.0,
        value=500.0
    )

    marketing = st.number_input(
        "Marketing Spend",
        min_value=0.0,
        value=100.0
    )

    if st.button("Predict Sales"):

        try:

            data = pd.DataFrame({
                "sales": [sales],
                "inventory": [inventory],
                "marketing": [marketing]
            })

            prediction = predict_sales(data)

            st.success(
                f"Forecasted Sales: {prediction[0]:.2f}"
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")