import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Dashboard")

file_path = "dataset/processed_sales.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    total_sales = (
        df["sales_amount"]
        .sum()
    )

    total_quantity = (
        df["quantity"]
        .sum()
    )

    avg_sales = (
        df["sales_amount"]
        .mean()
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Sales",
        f"₹ {round(total_sales,2)}"
    )

    c2.metric(
        "Total Quantity",
        total_quantity
    )

    c3.metric(
        "Average Sales",
        f"₹ {round(avg_sales,2)}"
    )

    st.subheader(
        "Sales by Product"
    )

    sales = (
        df.groupby("product")
        ["sales_amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        sales,
        x="product",
        y="sales_amount",
        title="Product Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Inventory Levels"
    )

    fig2 = px.pie(
        df,
        names="product",
        values="inventory"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.warning(
        "Processed data not found"
    )