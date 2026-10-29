record = input("Invoice record (CODE|QUANTITY|AMOUNT): ")

fields = record.split("|")

if len(fields) != 3:

    print("Malformed record: expected 3 fields.")

else:

    code = fields[0].strip()

    try:

        quantity = int(fields[1])

        amount = float(fields[2])

        if not code or quantity <= 0 or amount < 0:

            print("Invalid code, quantity or amount.")

        else:

            print("Product code:", code)

            print("Quantity:", quantity)

            print("Amount: Rs.", round(amount, 2))

    except ValueError:

        print("Quantity and amount must be numeric.")