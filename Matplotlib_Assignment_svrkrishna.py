import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Dataset 1: Study Hours vs Marks
# -----------------------------
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks_obtained = [45, 50, 55, 60, 68, 75, 82, 88, 92, 95]

# Task 1 - Part A: Line Plot
plt.figure(figsize=(8, 5))
plt.plot(study_hours, marks_obtained, color='blue', linestyle='-', marker='o')
plt.xlabel("Study Hours")
plt.ylabel("Marks Obtained")
plt.title("Student Performance Analysis")
plt.grid(True)
plt.show()

# Task 1 - Part B: Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, marks_obtained, color='red')
plt.xlabel("Study Hours")
plt.ylabel("Marks Obtained")
plt.title("Student Performance Analysis")
plt.grid(True)
plt.show()

# -----------------------------
# Dataset 2: Performance in Subjects
# -----------------------------
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
math_scores = [85, 78, 92, 88, 76]
science_scores = [78, 85, 88, 82, 90]

x = np.arange(len(students))
width = 0.35

# Task 2: Grouped Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(x - width/2, math_scores, width=width, color='blue', label='Math')
plt.bar(x + width/2, science_scores, width=width, color='orange', label='Science')
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Performance: Math vs Science")
plt.xticks(x, students)
plt.legend()
plt.grid(axis='y')
plt.show()

# -----------------------------
# Dataset 3: Marks Distribution
# -----------------------------
marks_distribution = [45, 52, 58, 63, 67, 71, 55, 60, 65, 70,
                      75, 80, 85, 90, 48, 54, 59, 64, 69, 74,
                      79, 84, 89, 50, 56, 62, 68, 72, 78, 83,
                      88, 46, 53, 61, 66, 73, 77, 82, 87, 92,
                      49, 57, 64, 70, 76, 81, 86, 91, 95, 51]

# Task 3 - Part A: Histogram
plt.figure(figsize=(8, 5))
plt.hist(marks_distribution, bins=10, color='green', edgecolor='black')
plt.title("Distribution of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.grid(axis='y')
plt.show()

# -----------------------------
# Dataset 4: Student Activities
# -----------------------------
activities = ['Sports', 'Music', 'Arts', 'Drama', 'Debate']
student_count = [45, 30, 25, 15, 35]
explode = [0.1, 0, 0, 0, 0]

# Task 3 - Part B: Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(student_count, labels=activities, autopct='%1.1f%%', explode=explode, startangle=90)
plt.title("Student Activity Distribution")
plt.show()

# -----------------------------
# Theory Answers
# -----------------------------
print("\nTASK 1: LINE PLOT AND SCATTER PLOT")
print("1. Difference between line plot and scatter plot:")
print("A line plot connects data points with lines to show trends or progression.")
print("A scatter plot shows only individual points and helps identify relationships, patterns, or outliers.")

print("\n2. When to prefer scatter plot over line plot:")
print("A scatter plot is preferred when we want to analyze individual observations and the relationship between two variables without connecting the points.")

print("\n3. Purpose of labels and titles:")
print("Labels explain what each axis represents, and the title tells the viewer what the graph is about. This makes the chart easy to understand.")

print("\nTASK 2: BAR CHART COMPARISON")
print("1. Why bar charts are useful:")
print("Bar charts are useful for comparing values across categories clearly and quickly.")

print("\n2. How grouped bars are created:")
print("Grouped bars are made by shifting one set of bars slightly left and another slightly right on the x-axis.")

print("\n3. Purpose of legend:")
print("The legend helps identify which color represents Math and which represents Science.")

print("\nTASK 3: HISTOGRAM AND PIE CHART")
print("1. What histograms tell us:")
print("Histograms show the overall distribution of data, such as concentration, spread, and patterns, which is harder to understand from a simple table.")

print("\n2. Meaning of bins:")
print("Bins are intervals used to group data values in a histogram. Choosing the right number of bins is important because too few can hide details and too many can make the graph confusing.")

print("\n3. When pie charts are appropriate and when to avoid them:")
print("Pie charts are appropriate when showing parts of a whole with a small number of categories.")
print("They should be avoided when there are too many categories or when values are very close, because comparison becomes difficult.")