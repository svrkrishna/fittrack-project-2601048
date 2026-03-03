# Task 1 Create and write student data
students = [
    "Alice,85",
    "Bob,92",
    "Charlie,78",
    "Diana,95"
]

file = open("students.txt", "w")

for student in students:
    file.write(student + "\n")

file.close()

print("Student records written successfully.")
