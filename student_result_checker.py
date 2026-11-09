student_name = input("Enter student name: ")
coursework = float(input("Enter coursework score (out of 30): "))
exam = float(input("Enter examination score (out of 70): "))

if coursework < 0 or coursework > 30 or exam < 0 or exam > 70:
    print("Invalid input.")
else:
    total = coursework + exam

    if total >= 70:
        grade = "A"
    elif total >= 60:
        grade = "B"
    elif total >= 50:
        grade = "C"
    elif total >= 45:
        grade = "D"
    elif total >= 40:
        grade = "E"
    else:
        grade = "F"

    if total >= 50:
        decision = "Pass"
    else:
        decision = "Resit required"

    print()
    print("STUDENT RESULT SUMMARY")
    print(f"Name: {student_name}")
    print(f"Coursework: {coursework:.2f} / 30")
    print(f"Examination: {exam:.2f} / 70")
    print(f"Total: {total:.2f} / 100")
    print(f"Grade: {grade}")
    print(f"Decision: {decision}")
