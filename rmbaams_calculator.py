import streamlit as st
from PIL import Image

# Set up branding
st.set_page_config(page_title="RMBAAMS Calculator", page_icon="💅", layout="centered", initial_sidebar_state="collapsed")

# Logo
logo = Image.open("New logo.png")
st.image(logo, width=200)

# Title
st.markdown("<h2 style='color: gold; text-align: center;'>Rakhi Maa Beauty Academy & Makeup Studio</h2>", unsafe_allow_html=True)
st.markdown("### 💰 INR to NPR Converter")
inr_amount = st.number_input("Enter amount in INR ₹", min_value=0.0, format="%.2f")
if st.button("Convert to NPR"):
    npr_amount = inr_amount * 1.6
    st.success(f"Equivalent NPR: Rs. {npr_amount:.2f}")

# Divider
st.markdown("---")

# Percentage Calculator
st.markdown("### 📊 Percentage Calculator")
base_amount = st.number_input("Enter base amount", min_value=0.0, format="%.2f")
percent = st.slider("Select percentage", 1, 100, 10)

if st.button("Calculate Percentage"):
    percent_value = base_amount * percent / 100
    final_amount = base_amount + percent_value
    st.info(f"➊ {percent}% of {base_amount:.2f} = {percent_value:.2f}")
    st.success(f"➋ Final Amount = {final_amount:.2f}")

# Footer
st.markdown("---")
st.markdown("<center>📍 Located at Jadibuti Chowk, Kathmandu | Call/WhatsApp: 9843503388</center>", unsafe_allow_html=True)
st.markdown("<center>📍 <a href='https://www.google.com/maps?q=jadibuti+chowk+kathmandu' target='_blank'>Google Maps link in bio</a></center>", unsafe_allow_html=True)
