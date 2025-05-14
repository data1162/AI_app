# modules/economics.py
def estimate_yield(crop, hectares):
    # Simulated yield data per hectare (tons) and market price per ton (₦)
    yield_data = {
        "Maize": {"yield_t_per_ha": 3.5, "price": 150000},
        "Rice": {"yield_t_per_ha": 4.0, "price": 180000},
        "Tomato": {"yield_t_per_ha": 6.0, "price": 70000},
        "Millet": {"yield_t_per_ha": 2.0, "price": 100000},
        "Cowpea": {"yield_t_per_ha": 1.8, "price": 200000},
        "Groundnut": {"yield_t_per_ha": 2.2, "price": 170000}
    }

    data = yield_data.get(crop)
    if not data:
        return "❌ Crop not found in economics model."

    yield_total = hectares * data["yield_t_per_ha"]
    gross_income = yield_total * data["price"]
    input_cost = hectares * 50000  # estimated input cost per ha
    profit = gross_income - input_cost

    return f"📊 Estimated Yield: {yield_total:.1f} tons\n💰 Gross Income: ₦{gross_income:,.0f}\n🧾 Estimated Cost: ₦{input_cost:,.0f}\n✅ Net Profit: ₦{profit:,.0f}"
