import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Exploratory Data Analysis")

file_path = "dataset/processed_sales.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    st.subheader("Dataset")

    st.dataframe(df.head())

    st.subheader("Sales Distribution")

    fig = px.histogram(
        df,
        x="sales_amount"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Product Sales")

    sales = (
        df.groupby("product")
        ["sales_amount"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        sales,
        x="product",
        y="sales_amount"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.warning(
        "Processed data not found"
    )