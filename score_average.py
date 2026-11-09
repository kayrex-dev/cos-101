# Calculate the total and average of several student scores.
student_count = int(input("How many students? "))

if student_count <= 0:
    print("The number of students must be greater than zero.")
else:
    total_score = 0.0

    for student_number in range(1, student_count + 1):
        score = float(input(f"Enter score for student {student_number}: "))
        total_score += score

    average_score = total_score / student_count

    print()
    print("CLASS SCORE SUMMARY")
    print("===================")
    print(f"Number of students: {student_count}")
    print(f"Total score: {total_score:.2f}")
    print(f"Average score: {average_score:.2f}")
