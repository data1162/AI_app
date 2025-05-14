# modules/security.py

STATES_AND_LGAS = {
    "Kano": ["Tarauni", "Dala", "Garko", "Rimin Gado"],
    "Kaduna": ["Chikun", "Birnin Gwari", "Zaria"],
    "Zamfara": ["Gusau", "Shinkafi", "Maru"],
    "Sokoto": ["Rabah", "Isa", "Wurno"],
    "Katsina": ["Jibia", "Batsari", "Kankia"],
    "Yobe": ["Damaturu", "Gujba", "Nguru"],
    "Bauchi": ["Alkaleri", "Misau", "Ningi"],
    "Benue": ["Makurdi", "Gboko", "Otukpo"],
    "Niger": ["Minna", "Bida", "Kontagora"],
    "Plateau": ["Jos North", "Barkin Ladi", "Pankshin"],
    "Adamawa": ["Yola North", "Gombi", "Numan"],
    "Kebbi": ["Birnin Kebbi", "Argungu", "Zuru"],
    "Borno": ["Maiduguri", "Biu", "Konduga"],
    "Nasarawa": ["Lafia", "Keffi", "Awe"]
}

INSECURE_AREAS = {
    "Kaduna": {
        "Birnin Gwari": ["Dogon Dawa", "Maganda"],
        "Chikun": ["Kajuru"]
    },
    "Zamfara": {
        "Shinkafi": ["Galadi"],
        "Maru": ["Dansadau"]
    },
    "Katsina": {
        "Jibia": ["Gidan Dawa"]
    },
    "Yobe": {
        "Gujba": ["Buni Yadi"]
    },
    "Borno": {
        "Konduga": ["Dalori"]
    },
    "Sokoto": {
        "Isa": ["Turba"]
    },
    "Benue": {
        "Gboko": ["Mbakinegh"]
    }
}

def get_threat_info(state, lga):
    threats = INSECURE_AREAS.get(state, {}).get(lga, [])
    if threats:
        return f"🚨 Threat zones in {lga}, {state}: {', '.join(threats)}. Avoid farming in these areas."
    else:
        return "✅ No major threats reported in this LGA."
