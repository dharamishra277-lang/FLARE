d = [["Rahul", 78, 88, 92],
     ["Priya", 65, 71, 69],
     ["Amit", 90, 94, 85],
     ["Sneha", 55, 60, 58],
     ["Vikram", 82, 79, 88]]

for x in d:
    avg = sum(x[1:]) / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    print(x[0], avg, grade)