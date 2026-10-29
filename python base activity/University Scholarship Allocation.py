applicants = [("Anu", 88, 82, 90, 92, 180000),

              ("Balu", 75, 78, 80, 88, 220000),

              ("Charan", 92, 70, 82, 86, 240000),

              ("Divya", 68, 90, 88, 95, 150000)]

eligible = []

for name, m, p, c, attendance, income in applicants:

    avg = (m + p + c) / 3

    if avg >= 75 and m >= 70 and attendance >= 85 and income <= 250000:

        eligible.append((avg, attendance, name))

eligible.sort(reverse=True)

print("SCHOLARSHIP MERIT LIST")

for rank, (avg, attendance, name) in enumerate(eligible, 1):

    print(rank, name, "Average:", round(avg, 2), "Attendance:", str(attendance)+"%")