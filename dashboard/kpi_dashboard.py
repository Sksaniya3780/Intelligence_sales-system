import streamlit as st


def show_kpi_dashboard():

    st.title("KPI Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Revenue",
            "$120,000",
            "+12%"
        )

    with col2:
        st.metric(
            "Orders",
            "1,250",
            "+5%"
        )

    with col3:
        st.metric(
            "Customers",
            "540",
            "+8%"
        )