#A student is allowed to write exams only if:Attendance is more than 75% AND has no disciplinary action.Evaluate eligibility based on input.
attendance = float(input("Enter attendance percentage: "))
disciplinary_action = input("Any disciplinary action? (yes/no): ").lower()

if attendance > 75 and disciplinary_action == "no":
    print("Eligible for exams.")
else:
    print("Not eligible for exams.")
