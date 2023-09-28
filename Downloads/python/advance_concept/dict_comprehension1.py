# Example 2: Dictionary Comprehension with if condition
student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eve': 88
}

top_students = {name: score for name, score in student_scores.items() if score > 90}

print(top_students)