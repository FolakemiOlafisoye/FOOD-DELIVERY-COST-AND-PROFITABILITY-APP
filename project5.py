import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

st.title("Food Delivery Cost & Profitability App")

# Define input parameters
st.subheader("Input Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    average_order_value = st.number_input("Average Order Value ($)", min_value=10, max_value=100, value=25)
with col2:
    delivery_fee = st.number_input("Delivery Fee ($)", min_value=2, max_value=10, value=5)
with col3:
    commission_rate = st.number_input("Commission Rate (%)", min_value=10, max_value=30, value=20)

# Define cost parameters
st.subheader("Cost Parameters")
col1, col2, col3 = st.columns(3)
with col1:
    food_cost = st.number_input("Food Cost (%)", min_value=20, max_value=50, value=30)
with col2:
    labor_cost = st.number_input("Labor Cost (%)", min_value=20, max_value=50, value=30)
with col3:
    marketing_cost = st.number_input("Marketing Cost (%)", min_value=5, max_value=20, value=10)

# Calculate revenue
revenue = average_order_value * 100

# Calculate costs
food_cost_amount = revenue * food_cost / 100
labor_cost_amount = revenue * labor_cost / 100
marketing_cost_amount = revenue * marketing_cost / 100
delivery_fee_revenue = revenue * delivery_fee / average_order_value
commission_amount = revenue * commission_rate / 100

# Calculate profitability
profit = revenue - food_cost_amount - labor_cost_amount - marketing_cost_amount - commission_amount
profit_margin = profit / revenue * 100

# Display results
st.subheader("Results")
col1, col2 = st.columns(2)
with col1:
    st.write(f"Revenue: ${revenue:.2f}")
    st.write(f"Food Cost: ${food_cost_amount:.2f}")
    st.write(f"Labor Cost: ${labor_cost_amount:.2f}")
    st.write(f"Marketing Cost: ${marketing_cost_amount:.2f}")
with col2:
    st.write(f"Delivery Fee Revenue: ${delivery_fee_revenue:.2f}")
    st.write(f"Commission Amount: ${commission_amount:.2f}")
    st.write(f"Profit: ${profit:.2f}")
    st.write(f"Profit Margin: ${profit_margin:.2f}%")

# Plot profitablity chart
st.subheader("Profitability Chart")
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(["Revenue", "Food Cost", "Labor Cost", "Marketing Cost", "Commission", "Profit"], [revenue, food_cost_amount,
labor_cost_amount, marketing_cost_amount, commission_amount, profit])
ax.set_title("Profitability Chart")
ax.set_xlabel("Category")
ax.set_ylabel("Amount ($)")
st.pyplot(fig)

# Interactive scenario planner
st.subheader("Scenario Planner")
average_order_value_scenario = st.number_input("Average Order Value Scenario ($)", min_value=10, max_value=100, value=25)
delivery_fee_scenario = st.number_input("Delivery Fee Scenario ($)", min_value=2, max_value=10, value=5)
commission_rate_scenario = st.number_input("Commission Rate Scenario (%)", min_value=10, max_value=30, value=20)

# Calculate scenario results
revenue_scenario = average_order_value_scenario * 100
profit_scenario = revenue_scenario - food_cost_amount - labor_cost_amount - marketing_cost_amount - commission_amount
profit_margin_scenario = profit_scenario / revenue_scenario * 100

# Display scenario results
st.write(f"Scenario Profit: ${profit_scenario:.2f}")
st.write(f"Scenario Profit Margin: ${profit_margin_scenario:.2f}%")