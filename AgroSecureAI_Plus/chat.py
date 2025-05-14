# chat.py – Multilingual Chatbot Interface
import streamlit as st
from modules.qa import answer_question
from modules.translator import detect_language, translate_to_english, translate_to_hausa

st.set_page_config(page_title="Farm Chatbot", layout="centered")
st.title("🤖 AgroSecure Chatbot – Ask Any Farming Question")

st.markdown("""
Type your farming question in English or Hausa. The chatbot will understand and respond in the same language.

Examples:
- What is the best seed for rice in Kaduna?
- Ta yaya zan kare tumatir daga cutar blight?
- When should I apply fertilizer for maize?
""")

user_input = st.text_input("📝 Your Question:")

if user_input:
    lang = detect_language(user_input)
    english_input = translate_to_english(user_input) if lang == "ha" else user_input
    raw_response = answer_question(english_input)
    final_response = translate_to_hausa(raw_response) if lang == "ha" else raw_response
    st.success(final_response)

st.markdown("---")
st.caption("Powered by AgroSecureAI+ Multilingual Simulation Engine")
