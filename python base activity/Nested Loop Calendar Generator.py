month = input("Month name: ")

days = int(input("Days in month (28-31): "))

start = int(input("Starting weekday (Mon=0, Sun=6): "))

if days < 28 or days > 31 or start < 0 or start > 6:

    print("Invalid month length or weekday.")

else:

    print(month)

    print("Mo Tu We Th Fr Sa Su")

    print("   " * start, end="")

    for date in range(1, days + 1):

        print(f"{date:2}", end=" ")

        if (start + date) % 7 == 0:

            print()

    print()