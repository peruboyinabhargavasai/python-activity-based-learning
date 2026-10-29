weight = float(input("Parcel weight (kg): "))

zone = input("Zone (local/regional/national): ").lower()

delivery = input("Delivery (standard/express): ").lower()

budget = float(input("Budget (Rs.): "))

zone_fee = {"local": 0, "regional": 50, "national": 100}

services = [("Standard", 40, 0), ("Express", 65, 40), ("Priority", 90, 80)]

if weight <= 0 or budget < 0 or zone not in zone_fee or delivery not in ("standard", "express"):

    print("Invalid input.")

else:

    eligible = []

    for name, rate, extra in services:

        if delivery == "standard" and name != "Standard":

            continue

        if delivery == "express" and name == "Standard":

            continue

        cost = weight * rate + zone_fee[zone] + extra

        print(name, "cost: Rs.", round(cost, 2))

        if cost <= budget:

            eligible.append((cost, name))

    if eligible:

        cost, name = min(eligible)

        print("Best eligible service:", name, "Cost: Rs.", round(cost, 2))

    else:

        print("No service fits the budget.")