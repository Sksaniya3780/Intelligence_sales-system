import streamlit as st
import pandas as pd

from preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline
)


def show_data_preprocessing():

    st.title("Data Preprocessing")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.subheader("Original Data")
            st.dataframe(df.head())

            if st.button("Run Preprocessing"):

                processed_df = (
                    PreprocessingPipeline.process(df)
                )

                st.subheader("Processed Data")
                st.dataframe(
                    processed_df.head()
                )

                csv = processed_df.to_csv(
                    index=False
                )

                st.download_button(
                    label="Download Processed CSV",
                    data=csv,
                    file_name="processed_sales.csv",
                    mime="text/csv"
                )

                st.success(
                    "Preprocessing completed successfully"
                )

        except Exception as e:
            st.error(
                f"Preprocessing Error: {e}"
            )


if __name__ == "__main__":
    show_data_preprocessing()