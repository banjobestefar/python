import math


def calculate_harvests(growth, regrowth, days_remaining):
    """
    Beregn antall høstinger per plante i løpet av sesongen.

    growth: antall dager til første høsting.
    regrowth: antall dager mellom påfølgende høstinger (None hvis avlingen ikke gjenvekster).
    days_remaining: antall dager som gjenstår i sesongen.
    """
    if regrowth is None:
        # For avlinger uten gjenvekst får du kun én høsting om det rekker å vokse
        return 1 if days_remaining >= growth else 0
    if days_remaining < growth:
        return 0
    # Første høsting skjer etter 'growth' dager
    remaining = days_remaining - growth
    # Antall påfølgende høstinger regnes ved å dele de gjenværende dagene på gjenvekstperioden
    additional = math.floor(remaining / regrowth)
    return 1 + additional


def main():
    # Database med eksempler på avlinger
    crops = {
        "cauliflower": {"seed_cost": 80, "growth": 12, "regrowth": None, "sale_price": 175},
        "blueberry": {"seed_cost": 80, "growth": 13, "regrowth": 4, "sale_price": 50},
        "tomato": {"seed_cost": 50, "growth": 11, "regrowth": 4, "sale_price": 60},
        "strawberry": {"seed_cost": 80, "growth": 13, "regrowth": 2, "sale_price": 100}
        ""
    }

    print("Jons Stardew kalkulator for Lina")
    print("--------------------------------------")
    print("Tilgjengelige avlinger:")
    for crop in crops:
        print(" -", crop.capitalize())

    chosen_crop = input("\nHvilken avling ønsker du å beregne? ").lower()
    if chosen_crop not in crops:
        print("Ugyldig. Finnes ikke i databasen.")
        return

    crop_info = crops[chosen_crop]

    try:
        days_remaining = int(input("Hvor mange dager gjenstår i sesongen? "))
        num_plants = int(input("Hvor mange frø skal du plante? "))
    except ValueError:
        print("Ugyldig.")
        return

    harvests = calculate_harvests(crop_info["growth"], crop_info["regrowth"], days_remaining)

    if harvests == 0:
        print("Det rekker ikke å høste denne avlingen i sesongen.")
        return

    total_revenue = harvests * crop_info["sale_price"] * num_plants
    total_seed_cost = crop_info["seed_cost"] * num_plants
    net_profit = total_revenue - total_seed_cost

    print("\nResultater for", chosen_crop.capitalize() + ":")
    print(f"  Antall mulige høstinger per plante: {harvests}")
    print(f"  Total inntekt: {total_revenue} guld")
    print(f"  Totale kostnader (frø): {total_seed_cost} guld")
    print(f"  Netto fortjeneste: {net_profit} guld")


if __name__ == "__main__":
    main()
