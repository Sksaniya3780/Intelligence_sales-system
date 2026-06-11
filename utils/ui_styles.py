import streamlit as st


def apply_custom_css():

    st.markdown(
        """
        <style>

        .stButton button {
            background-color:#4CAF50;
            color:white;
            border-radius:10px;
        }

        .stMetric {
            text-align:center;
        }

        </style>
        """,
        unsafe_allow_html=True
    )