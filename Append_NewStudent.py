# Task 3: Append new student and create log

# Append new student record
with open("students.txt", "a") as file:
    file.write("Eve,88\n")

print("New student added successfully.")

# Create log file
with open("activity.log", "w") as log_file:
    log_file.write("Added new student: Eve\n")

print("Log file created successfully.")
``
