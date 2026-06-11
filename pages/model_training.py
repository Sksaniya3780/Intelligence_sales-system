import streamlit as st
import subprocess
import os

st.title("🤖 Model Training")

if st.button("Train Model"):

    try:

        result = subprocess.run(
            ["python", "model/train_model.py"],
            capture_output=True,
            text=True
        )

        st.success(
            "Model Trained Successfully"
        )

        st.code(
            result.stdout
        )

    except Exception as e:

        st.error(str(e))

model_file = (
    "model/sales_forecast_model.pkl"
)

if os.path.exists(model_file):

    st.success(
        "Model Available"
    )

else:

    st.warning(
        "Model Not Trained"
    )