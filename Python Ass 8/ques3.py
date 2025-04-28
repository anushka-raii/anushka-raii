#Student Grades System

# Given dictionary
grades = {
    "Aanya": 89,
    "Ravi": 76,
    "Zoya": 92,
    "Kabir": 85
}

for student, grade in grades.items():
    print(f"{student}: {grade}")

top_student = max(grades, key=grades.get)
print(f"Top student is {top_student} with grade {grades[top_student]}")

