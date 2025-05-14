# modules/crop_advisor.py
import json
import pathlib

# Use a robust relative path to load crops.json
DATA_PATH = pathlib.Path(__file__).parent.parent / "data" / "crops.json"

try:
    with open(DATA_PATH, "r") as file:
        CROP_DATA = json.load(file)
except FileNotFoundError:
    CROP_DATA = {}

def get_crop_advice(crop, soil, state):
    if crop not in CROP_DATA:
        return "❌ Crop not found in database."

    data = CROP_DATA[crop]
    messages = [f"📌 Crop: {crop}"]

    # Seed Recommendation
    seed = data.get("seeds", {}).get(state, data.get("default_seed", "Unknown"))
    messages.append(f"🌱 Recommended Seed: {seed}")

    # Soil Suitability
    if soil.lower() != data.get("soil", "loamy").lower():
        messages.append(f"⚠️ Ideal soil for {crop} is {data['soil']}. Your selection: {soil}.")
    else:
        messages.append("✅ Suitable soil type selected.")

    # Fertilizer Advice
    messages.append(f"🧪 Fertilizer: {data.get('fertilizer', 'NPK 15-15-15 after 2 weeks')}")

    # Pesticide Advice
    messages.append(f"💊 Pesticide: {data.get('pesticide', 'Use safe pesticide for common pests')}")

    # Inspection Times
    inspections = data.get("inspection_days", ["14 days", "45 days", "75 days"])
    messages.append(f"📆 Inspection Times: {', '.join(inspections)}")

    return "\n".join(messages)
