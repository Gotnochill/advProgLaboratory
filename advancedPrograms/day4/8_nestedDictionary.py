# Create a nested dictionary for department → students → marks
departments = {
    'CSE': {
        'Alice': 85,
        'Bob': 90
    },
    'ECE': {
        'Charlie': 78,
        'David': 88
    }
}
print("Nested dictionary:")
for dept, students in departments.items():
    print(dept)
    for student, marks in students.items():
        print(f"  {student}: {marks}")
