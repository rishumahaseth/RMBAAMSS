import streamlit as st
from PIL import Image

# Set up branding
st.set_page_config(page_title="RMBAAMS Calculator", page_icon="💅", layout="centered", initial_sidebar_state="collapsed")

# Title
st.markdown("<h2 style='color: gold; text-align: center;'>Rakhi Maa Beauty Academy & Makeup Studio</h2>", unsafe_allow_html=True)

# INR to NPR Converter
st.markdown("### 💰 INR to NPR Converter")
inr_amount = st.number_input(
    "Enter amount in INR ₹",
    min_value=0.0,
    step=1.0,
    value=None,  # No default value to avoid showing 0.00
    placeholder="Type INR amount..."
)
if st.button("Convert to NPR"):
    if inr_amount is not None:  # Check if the user has entered a value
        npr_amount = inr_amount * 1.6
        st.success(f"Equivalent NPR: Rs. {npr_amount:.2f}")

# Divider
st.markdown("---")

# Percentage Calculator
st.markdown("### 📊 Percentage Calculator")
base_amount = st.number_input(
    "Enter base amount",
    min_value=0.0,
    step=1.0,
    value=None,  # No default value to avoid showing 0.00
    placeholder="Enter amount here..."
)

# Dropdown instead of slider
percent = st.selectbox(
    "Select percentage",
    options=[i for i in range(1, 101)],
    index=9  # Default is 10%
)

if st.button("Calculate Percentage"):
    if base_amount is not None:  # Check if the user has entered a value
        percent_value = base_amount * percent / 100
        final_amount = base_amount + percent_value
        st.info(f"➊ {percent}% of {base_amount:.2f} = {percent_value:.2f}")
        st.success(f"➋ Final Amount = {final_amount:.2f}")

# Footer
st.markdown("---")
