



students = [
    {"name": "Alice", "grade": 91, "major": "CS"},
    {"name": "Bob", "grade": 54, "major": "Math"},
    {"name": "Carol", "grade": 78, "major": "CS"},
    {"name": "David", "grade": 63, "major": "Art"},
    {"name": "Eve", "grade": 45, "major": "Math"},
    {"name": "Frank", "grade": 88, "major": "CS"},
]



def get_passing_students(students):
    passing = []

    for student in students:
        if student["grade"] >= 60:
            passing.append(student)

    return passing



def get_average_grade(students):
    if len(students) == 0:
        return 0

    total = 0

    for student in students:
        total += student["grade"]

    return total / len(students)



def count_by_major(students):
    counts = {}

    for student in students:
        major = student["major"]
        counts[major] = counts.get(major, 0) + 1

    return counts



def get_top_student(students):
    if len(students) == 0:
        return None

    top_student = students[0]

    for student in students:
        if student["grade"] > top_student["grade"]:
            top_student = student

    return top_student



def filter_by_major(students, major):
    result = []

    for student in students:
        if student["major"] == major:
            result.append(student)

    return result



def main():
    print("--- Student Report ---")

    print(f"Total students: {len(students)}")

    passing = get_passing_students(students)
    print(f"Passing students: {len(passing)}")

    print("\nPassing students:")
    for student in passing:
        print(f"  {student['name']} - {student['grade']}")

    avg = get_average_grade(students)
    print(f"\nAverage grade: {avg:.2f}")

    print(f"Students by major: {count_by_major(students)}")

    top = get_top_student(students)

    if top is not None:
        print(f"Top student: {top['name']} ({top['grade']})")

    print("\nCS students:")

    for student in filter_by_major(students, "CS"):
        print(f"  {student['name']} - {student['grade']}")



main()