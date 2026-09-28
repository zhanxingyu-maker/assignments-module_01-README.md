

count = int(input("How many students? "))

while count < 1 or count > 50:
    count = int(input("Invalid. Enter a number between 1 and 50: "))



scores = []

for student in range(1, count + 1):

    score = int(input(f"Enter score for student {student} (0-100): "))

    # Step 3 - Handle absent student
    if score == -1:
        print(f"Skipping student {student}")
        continue

    # Step 4 - Handle early exit
    if score == 999:
        print("Early exit triggered.")
        break

    # Validate the score
    while score < 0 or score > 100:
        score = int(input("Invalid score. Try again: "))

        # Check for absent student again
        if score == -1:
            print(f"Skipping student {student}")
            break

        # Check for early exit again
        if score == 999:
            print("Early exit triggered.")
            break

   
    if score == -1:
        continue

    if score == 999:
        break

    scores.append(score)




print("\n--- Student Grades ---")

student_number = 1

for score in scores:

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student {student_number}: {score} → {grade}")

    student_number += 1




print("\n--- Class Statistics ---")

if len(scores) > 0:

    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    passed = 0
    failed = 0

    for score in scores:
        if score >= 60:
            passed += 1
        else:
            failed += 1

    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {passed} | Failed: {failed}")

else:
    print("No scores were collected.")