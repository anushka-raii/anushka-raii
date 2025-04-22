 #Engineering Grading System:Take student’s marks as input and classify: Distinction ≥ 75 ,First Class 60–74 ,Pass 35–59 Fail < 35

marks = float(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif 60 <= marks < 75:
    print("First Class")
elif 35 <= marks < 60:
    print("Pass")
else:
    print("Fail")
