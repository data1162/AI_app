# modules/weather.py
import requests
import streamlit as st

def get_weather_forecast(location):
    api_key = st.secrets["OPENWEATHER_API"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location},NG&appid={api_key}&units=metric"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        return f"📍 {location} Weather: {desc}, 🌡️ {temp}°C, 💧 Humidity: {humidity}%"
    else:
        return "⚠️ Weather data unavailable. Please check your API key or internet connection."

def get_rain_forecast(location):
    api_key = st.secrets["OPENWEATHER_API"]
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location},NG&appid={api_key}&units=metric"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        rain_coming = any("rain" in entry and entry['rain'].get('3h', 0) > 0 for entry in data['list'][:8])
        if rain_coming:
            return "🌧️ Rain expected in the next 24 hours."
        else:
            return "☀️ No rain expected in the next 24 hours."
    else:
        return "⚠️ Rain forecast unavailable."
