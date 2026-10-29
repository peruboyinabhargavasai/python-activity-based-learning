n = int(input("Diamond size (1-20): "))

if n < 1 or n > 20:

    print("Size must be from 1 to 20.")

else:

    for row in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):

        spaces = " " * (n - row)

        if row == 1:

            print(spaces + "*")

        else:

            print(spaces + "*" + " " * (2 * row - 3) + "*")