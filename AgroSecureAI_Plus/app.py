# app.py – Start of your offline farming expert app
import streamlit as st
from modules.crop_advisor import get_crop_advice
from modules.weather import get_weather_forecast
from modules.security import get_threat_info, STATES_AND_LGAS
from modules.economics import estimate_yield
from modules.qa import answer_question

st.set_page_config(page_title="AgroSecure AI+", layout="centered")
st.title("🌾 AgroSecure AI+ – Nigerian Farming Assistant")

mode = st.sidebar.radio("Select Mode", ["📊 Farming Dashboard", "🤖 Ask Farming Questions"])

if mode == "📊 Farming Dashboard":
    st.subheader("🧭 Select Your Farming Location and Crop")
    state = st.selectbox("State", list(STATES_AND_LGAS.keys()))
    lga = st.selectbox("Local Government Area", STATES_AND_LGAS[state])
    crop = st.selectbox("Crop", ["Maize", "Rice", "Millet", "Tomato", "Cowpea", "Groundnut", "Sorghum", "Soybean", "Onion"])
    soil = st.selectbox("Soil Type", ["Loamy", "Sandy", "Clay", "Other"])
    hectares = st.number_input("Farm Size (hectares)", min_value=0.1, step=0.1, value=1.0)

    if st.button("🔍 Analyze"):
        weather = get_weather_forecast(lga)
        advice = get_crop_advice(crop, soil, state)
        threats = get_threat_info(state, lga)
        yield_est = estimate_yield(crop, hectares)

        st.subheader("🌱 Crop & Input Advice")
        st.write(advice)

        st.subheader("🌦️ Weather Forecast")
        st.write(weather)

        st.subheader("🛡️ Security Risk")
        st.write(threats)

        st.subheader("💰 Revenue Estimate")
        st.write(yield_est)

elif mode == "🤖 Ask Farming Questions":
    st.subheader("Ask About Crop Issues, Pests, Fertilizer Use...")
    query = st.text_input("Your question")
    if query:
        response = answer_question(query)
        st.write(response)
