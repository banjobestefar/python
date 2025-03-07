import random


def roll_dice():
    # Simulerer to terningkast
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def get_resource(roll):
    # Hvis terningkastet er 7, får du ingen ressurs.
    if roll == 7:
        return None
    resources = ['wood', 'brick', 'wool', 'grain', 'ore']
    return random.choice(resources)


def can_build(cost, resources):
    # Sjekker om du har nok ressurser til å bygge
    for res, amount in cost.items():
        if resources.get(res, 0) < amount:
            return False
    return True


def build(cost, resources):
    # Trekker fra ressursene du bruker til bygging
    for res, amount in cost.items():
        resources[res] -= amount


def print_resources(resources):
    print("Dine ressurser:")
    for res, amount in resources.items():
        print(f"  {res}: {amount}")


def main():
    resources = {'wood': 0, 'brick': 0, 'wool': 0, 'grain': 0, 'ore': 0}
    victory_points = 0

    print("Velkommen til Min Mini Settlers!")
    print("Målet er å oppnå 5 seierspoeng ved å bygge landsbyer og byer.")
    print("Byggekostnader:")
    print("  landsby: 1 wood, 1 brick, 1 wool, 1 grain (gir 1 seierspoeng)")
    print("  By: 2 grain, 3 ore (oppgrader landsby, gir 1 ekstra seierspoeng)")

    settlement_cost = {'wood': 1, 'brick': 1, 'wool': 1, 'grain': 1}
    city_cost = {'grain': 2, 'ore': 3}

    while victory_points < 5:
        print("\nVelg et alternativ:")
        print("  1. Kast terningene for å samle ressurs")
        print("  2. Bygg landsby")
        print("  3. Bygg by (oppgrader landsby)")
        print("  4. Vis ressurser")
        print("  5. Avslutt")
        valg = input("Ditt valg: ")

        if valg == "1":
            roll = roll_dice()
            print(f"Du kastet: {roll}")
            resource = get_resource(roll)
            if resource:
                resources[resource] += 1
                print(f"Du fikk 1 {resource}!")
            else:
                print("Røver! Ingen ressurs til deg.")
        elif valg == "2":
            if can_build(settlement_cost, resources):
                build(settlement_cost, resources)
                victory_points += 1
                print("Du bygde en landsby og fikk 1 seierspoeng!")
            else:
                print("Du har ikke nok ressurser til å bygge en landsby.")
        elif valg == "3":
            if can_build(city_cost, resources):
                build(city_cost, resources)
                victory_points += 1
                print("Du oppgraderte en landsby til en by og fikk 1 ekstra seierspoeng!")
            else:
                print("Du har ikke nok ressurser til å bygge en by.")
        elif valg == "4":
            print_resources(resources)
            print(f"Seierspoeng: {victory_points}")
        elif valg == "5":
            print("Avslutter spillet.")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

    if victory_points >= 5:
        print("\nGratulerer! Du har vunnet spillet med 5 seierspoeng!")


if __name__ == "__main__":
    main()
