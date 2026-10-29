distance = float(input("Distance in km: "))

name = input("Passenger name: ")

age = int(input("Age: "))

travel_class = input("Class (sleeper/ac3/ac2): ").lower()

rates = {"sleeper": 1, "ac3": 2, "ac2": 3}

fees = {"sleeper": 20, "ac3": 40, "ac2": 50}

if distance <= 0 or age < 0 or travel_class not in rates:

    print("Invalid input.")

else:

    base = distance * 1.2 * rates[travel_class]

    concession = base * 0.20 if age >= 60 else 0

    total = base - concession + fees[travel_class]

    print("Passenger:", name)

    print("Base fare: Rs.", round(base, 2))

    print("Concession: Rs.", round(concession, 2))

    print("Reservation: Rs.", fees[travel_class])

    print("Final fare: Rs.", round(total, 2))