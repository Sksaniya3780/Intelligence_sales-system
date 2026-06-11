import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="Intelligent Sales Forecasting System",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Intelligent Sales Forecasting & Inventory Optimization System")

st.markdown("""
### Features
- Sales Data Management
- Inventory Tracking
- Sales Forecasting
- Inventory Optimization
- KPI Dashboard
- PDF Reports
""")

st.sidebar.success("Select a module from Pages folder")

try:
    conn = sqlite3.connect("database/sales.db")
    df = pd.read_sql("SELECT * FROM sales_data", conn)

    st.subheader("Latest Sales Data")

    st.dataframe(df.head())

    st.metric(
        "Total Sales",
        f"₹ {round(df['sales_amount'].sum(),2)}"
    )

except Exception as e:
    st.warning("Database not initialized yet.")
    st.error(e)