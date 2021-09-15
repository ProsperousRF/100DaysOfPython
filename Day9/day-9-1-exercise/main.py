student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    # 91 - 100: Grade = "Outstanding"
    if score >= 91:
        grade = "Outstanding"
    # 81 - 90: Grade = "Exceeds Expectations"
    elif score in range(81, 91):
        grade = "Exceeds Expectations"
    # 71 - 80: Grade = "Acceptable"
    elif score in range(71, 81):
        grade = "Acceptable"
    # 70 or lower: Grade = "Fail"
    else:
        grade = "Fail"
    student_grades[key] = grade


# 🚨 Don't change the code below 👇
print(student_grades)
