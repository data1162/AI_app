# modules/translator.py
from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text

def translate_to_hausa(text):
    try:
        return GoogleTranslator(source='auto', target='ha').translate(text)
    except:
        return text
