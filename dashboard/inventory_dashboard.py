import streamlit as st


def show_inventory_dashboard():

    st.title("Inventory Dashboard")

    st.subheader("Current Inventory Status")

    inventory = {
        "Product A": 150,
        "Product B": 80,
        "Product C": 30
    }

    st.table(inventory)

       