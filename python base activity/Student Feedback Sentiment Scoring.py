feedback = input("Feedback: ").lower()

for mark in ".,!?;:":

    feedback = feedback.replace(mark, " ")

words = feedback.split()

positive = ["good", "helpful", "excellent", "clear", "useful"]

negative = ["bad", "confusing", "poor", "difficult", "boring"]

pos = sum(1 for word in words if word in positive)

neg = sum(1 for word in words if word in negative)

score = pos - neg

if score > 0:

    category = "Positive"

elif score < 0:

    category = "Negative"

else:

    category = "Neutral"

print("Positive keywords:", pos)

print("Negative keywords:", neg)

print("Score:", score)

print("Category:", category)