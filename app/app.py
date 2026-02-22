import streamlit as st
import numpy as np
import pickle
import os

# ---------- Load Model ----------
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "model.pkl")
model = pickle.load(open(model_path, "rb"))

# ---------- Page Config ----------
st.set_page_config(page_title="Milk Quality Predictor", page_icon="🥛", layout="centered")

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>🥛 Milk Quality Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>AI-powered food safety analysis</p>", unsafe_allow_html=True)

st.divider()

# ---------- Input Section ----------
st.subheader("🔍 Enter Milk Parameters")

col1, col2 = st.columns(2)

with col1:
    pH = st.slider("pH Level", 0.0, 14.0, 6.5)
    Temperature = st.slider("Temperature (°C)", 0, 100, 25)
    Taste = st.radio("Taste", ["Bad", "Good"])

with col2:
    Odor = st.radio("Odor", ["Bad", "Good"])
    Fat = st.radio("Fat Level", ["Low", "High"])
    Turbidity = st.radio("Turbidity", ["Low", "High"])

Colour = st.slider("Colour Value", 200, 255, 230)

# Convert categorical to numeric
taste_val = 1 if Taste == "Good" else 0
odor_val = 1 if Odor == "Good" else 0
fat_val = 1 if Fat == "High" else 0
turbidity_val = 1 if Turbidity == "High" else 0

st.divider()

# ---------- Prediction ----------
if st.button("🚀 Predict Quality", use_container_width=True):

    with st.spinner("Analyzing milk quality..."):
        input_data = np.array([[pH, Temperature, taste_val, odor_val, fat_val, turbidity_val, Colour]])
        prediction = model.predict(input_data)[0]

    st.subheader("📊 Result")

    # ---------- Result + Recommendation ----------
    if prediction == 0:
        st.error("❌ Low Quality Milk")
        st.progress(30)
        recommendation = "Do not consume ❌"
        farmer_advice = "Milk may be spoiled. Avoid selling or consuming."

    elif prediction == 1:
        st.warning("⚠️ Medium Quality Milk")
        st.progress(60)
        recommendation = "Boil before use ⚠️"
        farmer_advice = "Milk is usable after proper boiling."

    else:
        st.success("✅ High Quality Milk")
        st.progress(90)
        recommendation = "Safe to sell ✅"
        farmer_advice = "Milk is fresh and safe for selling."

    # 🎉 animation
    st.balloons()

    # ---------- Recommendation Section ----------
    st.markdown("### 🧠 Recommendation")
    st.info(recommendation)

    # ---------- Farmer Advice ----------
    st.markdown("### 👨‍🌾 Advice for Farmers")
    st.write(farmer_advice)

    # ---------- Explanation Section ----------
    with st.expander("ℹ️ Why this result?"):
        st.write(f"""
        - pH Level: {pH}
        - Temperature: {Temperature}°C
        - Taste: {Taste}
        - Odor: {Odor}
        - Fat Level: {Fat}
        - Turbidity: {Turbidity}
        - Colour Value: {Colour}

        The machine learning model analyzed these parameters to determine milk quality.
        """)
