name = input("What is your name? ")
age = int(input("How old are you? "))
gpa = float(input("What is your GPA? "))

birth_year = 2026 - age

print("--- Student Profile ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Approximate birth year: {birth_year}")
print(f"GPA: {gpa:.2f}")

if gpa >= 3.5:
    print("GPA status: Excellent")
elif gpa >= 3.0:
    print("GPA status: Good")
elif gpa >= 2.0:
    print("GPA status: Satisfactory")
else:
    print("GPA status: Needs improvement")
