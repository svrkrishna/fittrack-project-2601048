def calculate_grade(*scores, **adjustments):
    if not scores:
        return 0.0

    # Calculate average of scores
    average = sum(scores) / len(scores)

    # Add all bonus adjustments
    bonus_total = sum(adjustments.values())

    final_grade = average + bonus_total

    return float(final_grade)


n = int(input("How many scores? "))

scores = []
for i in range(n):
    scores.append(float(input(f"Enter score {i+1}: ")))

attendance = float(input("Attendance bonus (enter 0 if none): "))
project = float(input("Project bonus (enter 0 if none): "))

final = calculate_grade(*scores, attendance=attendance, project=project)
print(f"Final Grade: {final:.2f}%")
