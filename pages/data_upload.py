import streamlit as st
import pandas as pd
import os

st.title("📂 Data Upload")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("File Uploaded Successfully")

    st.dataframe(df.head())

    save_path = "dataset/sales_data.csv"

    df.to_csv(
        save_path,
        index=False
    )

    st.success(
        f"Saved to {save_path}"
    )