# stdeval.py
# Usage: python stdeval.py <name> <score1> <score2> <score3>

import sys

def usage_and_exit():
    print("Usage: python stdeval.py <name> <score1> <score2> <score3>")
    sys.exit(2)

def compute_grade(avg):
    # simple grading scale — change as needed
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    return "F"

if len(sys.argv) != 5:
    print("Error: wrong number of arguments.")
    usage_and_exit()

name = sys.argv[1]
raw_scores = sys.argv[2:5]

# convert to float (or int) with validation
scores = []
for i, rs in enumerate(raw_scores, start=1):
    try:
        # allow integer or float scores
        val = float(rs)
        # optional: ensure score in 0-100
        if val < 0 or val > 100:
            print(f"Error: score{i} out of range (0-100): {val}")
            sys.exit(3)
        scores.append(val)
    except ValueError:
        print(f"Error: score{i} is not a number: '{rs}'")
        usage_and_exit()

total = sum(scores)
avg = total / 3.0

grade = compute_grade(avg)

# Output in a simple, Jenkins-friendly way
print(f"Student: {name}")
print(f"Scores: {scores[0]} , {scores[1]} , {scores[2]}")
print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")

# exit 0 -> success
sys.exit(0)
