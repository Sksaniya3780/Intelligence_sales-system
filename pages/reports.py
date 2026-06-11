import streamlit as st
import pandas as pd
import os

st.title("📄 Reports")

file_path = "dataset/processed_sales.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    st.subheader("Processed Sales Report")

    st.dataframe(df)

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="sales_report.csv",
        mime="text/csv"
    )

else:

    st.warning(
        "No processed data found"
    )