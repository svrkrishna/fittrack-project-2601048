# Task 2: Read and display student data

try:
    with open("students.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            name, score = line.strip().split(",")
            print(f"Student: {name}, Score: {score}")

except FileNotFoundError:
    print("Error: students.txt file not found.")
