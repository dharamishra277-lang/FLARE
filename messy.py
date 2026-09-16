students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88]
]


def calculate_grade(average):
    """Return the grade based on the average marks."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_report(student_data):
    """Calculate and display each student's average and grade."""
    for student in student_data:
        name = student[0]
        marks = student[1:]
        average = sum(marks) / 3
        grade = calculate_grade(average)

        print(name, average, grade)


generate_report(students)