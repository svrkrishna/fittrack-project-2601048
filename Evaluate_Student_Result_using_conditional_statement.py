# evaluate a student's result using conditional statements
Student_name = input("Enter student name: ")
Maths = int(input("Enter Maths marks: "))
Science = int(input("Enter Science marks: "))
English = int(input("Enter English marks: "))
# Validate the marks
if (Maths < 0 or Maths > 100 or
    Science < 0 or Science > 100 or
        English < 0 or English > 100):
    print("Invalid marks entered")
else:
    # Calculation
    Total_Marks = Maths + Science + English
    Average = Total_Marks / 3
    # pass/Fail
    if Maths < 40 or Science < 40 or English < 40:
        status = "Fail"
    else:
        status = "Pass"
# Output
    print(f"\nStudent name: {Student_name}")
    print(f"\nTotal marks: {Total_Marks}")
    print(f"\npercentage: {Average:.2f}")
    print(f"\nstatus: {status}")
# Assign_Grade
    if status == "Pass":
        if Average >= 75:
            Grade = "A"
        elif Average >= 60:
            Grade = "B"
        else:
            Grade = "C"
        print(f"\nGrade:{Grade}")
