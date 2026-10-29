vehicle = input("Vehicle (bike/car): ").lower()

offence = input("Offence (speeding/helmet/signal): ").lower()

repeat = input("Repeat offence? (yes/no): ").lower()

count = int(input("Total violations: "))

fines = {"speeding": 1000, "helmet": 500, "signal": 1500}

if vehicle not in ("bike", "car") or offence not in fines or repeat not in ("yes", "no") or count < 0:

    print("Invalid input.")

else:

    fine = fines[offence] * (2 if repeat == "yes" else 1)

    status = "Review required" if count >= 3 else "Normal review"

    print("Vehicle:", vehicle.title())

    print("Offence:", offence.title())

    print("Sample fine: Rs.", fine)

    print("Case status:", status)