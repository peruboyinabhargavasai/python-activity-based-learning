paragraph = input("Enter paragraph: ").lower()

for mark in ".,!?;:()":

    paragraph = paragraph.replace(mark, " ")

words = paragraph.split()

seen = []

found = False

for word in words:

    if word not in seen:

        seen.append(word)

        positions = [i + 1 for i, item in enumerate(words) if item == word]

        if len(positions) > 1:

            found = True

            print(word, "count:", len(positions), "positions:", positions)

if not found:

    print("No repeated words found.")