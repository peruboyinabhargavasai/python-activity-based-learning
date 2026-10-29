email = input("Student email: ").strip()

reg_id = input("Registration ID (CSE1234): ").strip().upper()

errors = []

if " " in email:

    errors.append("Email must not contain spaces.")

if email.count("@") != 1:

    errors.append("Email must contain exactly one @.")

elif "." not in email.split("@")[1]:

    errors.append("Email domain must contain a dot.")

if not reg_id.startswith("CSE") or len(reg_id) != 7 or not reg_id[3:].isdigit():

    errors.append("ID must start with CSE and end in four digits.")

if errors:

    print("Invalid record:")

    for error in errors:

        print("-", error)

else:

    print("Email format: Valid")

    print("Registration ID: Valid")