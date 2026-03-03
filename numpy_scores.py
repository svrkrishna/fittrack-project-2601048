import numpy as np

# -------------------------
# Task 1 — Generate + Inspect
# -------------------------
np.random.seed(42)

# random integers between 50 and 100 (inclusive) => high must be 101
scores = np.random.randint(50, 101, size=(5, 4))

print("scores:\n", scores)

# The score of the 3rd student in the 2nd subject (0-based indexing => [2, 1])
print("\nTask 1.1 - 3rd student, 2nd subject:", scores[2, 1])

# All scores of the last 2 students (all subjects)
print("\nTask 1.2 - Last 2 students (all subjects):\n", scores[-2:, :])

# All scores for the first 3 students in subjects 2 and 3 only
# subjects 2 and 3 => indices 1 and 2
print("\nTask 1.3 - First 3 students, subjects 2 and 3:\n", scores[:3, 1:3])

# -------------------------
# Task 2 — Analyze with Broadcasting (no loops)
# -------------------------
col_means = np.round(scores.mean(axis=0), 2)
print("\nTask 2.1 - Column-wise mean (per subject), rounded to 2 decimals:", col_means)

curve = np.array([5, 3, 7, 2])  # one per subject
curved_scores = scores + curve  # broadcasting across rows
curved_scores = np.clip(curved_scores, 0, 100)  # ensure no score exceeds 100

print("\nTask 2.2 - curved_scores (clipped to 100):\n", curved_scores)

row_max = curved_scores.max(axis=1)
print("\nTask 2.3 - Row-wise max (best subject per student):", row_max)

# -------------------------
# Task 3 — Normalize + Identify
# -------------------------
row_min = curved_scores.min(axis=1, keepdims=True)
row_max2 = curved_scores.max(axis=1, keepdims=True)

# Avoid divide-by-zero in the unlikely case row_max == row_min
denom = np.where((row_max2 - row_min) == 0, 1, (row_max2 - row_min))
normalized = (curved_scores - row_min) / denom

print("\nTask 3.1 - Min-max normalized per row:\n", normalized)

# single highest value across entire normalized array
flat_idx = np.argmax(normalized)
student_idx, subject_idx = np.unravel_index(flat_idx, normalized.shape)

print("\nTask 3.2 - Highest normalized value at (student, subject):",
      (student_idx, subject_idx))
print("Highest normalized value:", normalized[student_idx, subject_idx])

# all scores from curved_scores strictly above 90 as 1D array
above_90 = curved_scores[curved_scores > 90].ravel()
print("\nTask 3.3 - curved_scores values > 90 (1D):", above_90)
