import streamlit as st
from model.predict import predict_sales

st.title("📈 Sales Forecasting")

st.subheader("Enter Forecast Inputs")

quantity = st.number_input(
    "Quantity Sold",
    min_value=1,
    value=10
)

inventory = st.number_input(
    "Inventory",
    min_value=1,
    value=50
)

month = st.slider(
    "Month",
    1,
    12,
    6
)

day = st.slider(
    "Day",
    1,
    31,
    15
)

day_of_week = st.slider(
    "Day Of Week",
    0,
    6,
    2
)

quarter = st.slider(
    "Quarter",
    1,
    4,
    2
)

if st.button("Predict Sales"):

    try:

        prediction = predict_sales(
            quantity,
            inventory,
            month,
            day,
            day_of_week,
            quarter
        )

        st.success(
            f"Predicted Sales: ₹ {round(prediction,2)}"
        )

    except Exception as e:

        st.error(str(e))