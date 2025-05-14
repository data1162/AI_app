# modules/qa.py – Smart Simulation-based Expert Q&A

def answer_question(query):
    query = query.lower()

    # Topic categories using keyword match logic
    if "maize" in query and ("seed" in query or "variety" in query):
        return "🌱 Use SAMMAZ 52 in Kano, SAMMAZ 40 in Kaduna. Choose based on your state's agro zone."

    if "tomato" in query and ("yellow" in query or "leaves" in query):
        return "🍅 Yellowing leaves in tomato may mean nitrogen deficiency or early blight. Apply NPK and Ridomil."

    if "cowpea" in query and ("pest" in query or "worm" in query):
        return "🐛 Use Cypermethrin to control Maruca and aphids in cowpea. Apply every 2 weeks during flowering."

    if "fertilizer" in query and ("rice" in query or "when" in query):
        return "💧 Apply NPK before transplanting rice. Add Urea 3 weeks later for better yield."

    if ("groundnut" in query or "peanut" in query) and "soil" in query:
        return "🧱 Groundnut prefers sandy soil with good drainage and low acidity."

    if "rain" in query and ("when" in query or "start" in query):
        return "🌧️ In Northern Nigeria, rains typically begin in late May to early June. Check weather forecasts weekly."

    if "inspect" in query and "millet" in query:
        return "📆 Inspect millet at 12, 40, and 75 days after planting. Look for drought signs and grasshoppers."

    if "blight" in query and "tomato" in query:
        return "🦠 For tomato blight, spray Ridomil Gold or Mancozeb every 10 days especially in rainy season."

    if "safe" in query and ("zamfara" in query or "shinkafi" in query):
        return "🛡️ Avoid farming in Galadi (Shinkafi LGA, Zamfara) due to reported insecurity."

    if "profit" in query and "maize" in query:
        return "💰 A 1-hectare maize farm can yield 3.5 tons and return over ₦500,000 profit if inputs are optimized."

    if "best soil" in query and "rice" in query:
        return "🌾 Rice grows best in clay or silty soil with good water retention. Upland rice needs less flooding."

    if "harvest" in query and "cowpea" in query:
        return "🧺 Harvest cowpea 70–75 days after planting, once pods turn dry and brown."

    if "which pesticide" in query and ("maize" in query or "insect" in query):
        return "💊 Use Lambda-cyhalothrin or Emamectin benzoate for insect control in maize."

    if "how many tons" in query and ("rice" in query or "yield" in query):
        return "📊 Rice yield is about 4 tons per hectare under good management."

    if "onion" in query and ("storage" in query or "preserve" in query):
        return "🧅 Store onion in dry, ventilated baskets or mesh bags. Avoid stacking too high."

    if "soybean" in query and "planting time" in query:
        return "📅 Plant soybean early June in northern regions. Use TGX 1835-10E for high yield."

    return "🤖 Sorry, I couldn't understand your question exactly. Try asking about seeds, pests, fertilizer, soil, or rainfall."
