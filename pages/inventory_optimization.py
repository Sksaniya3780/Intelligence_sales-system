import streamlit as st

from inventory_optimizer.safety_stock import SafetyStockCalculator
from inventory_optimizer.reorder_calculator import ReorderCalculator

st.title("📦 Inventory Optimization")

avg_demand = st.number_input(
    "Average Daily Demand",
    min_value=1,
    value=20
)

lead_time = st.number_input(
    "Lead Time (Days)",
    min_value=1,
    value=7
)

if st.button("Optimize Inventory"):

    safety_stock = (
        SafetyStockCalculator
        .calculate_safety_stock(
            avg_demand,
            lead_time
        )
    )

    reorder_point = (
        ReorderCalculator
        .calculate_reorder_point(
            avg_demand,
            lead_time,
            safety_stock
        )
    )

    st.metric(
        "Safety Stock",
        safety_stock
    )

    st.metric(
        "Reorder Point",
        reorder_point
    )