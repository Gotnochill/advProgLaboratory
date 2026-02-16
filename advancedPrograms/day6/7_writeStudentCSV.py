# 7. Store student records in a CSV file
import csv
filename = "students.csv"
fields = ['Name', 'Age', 'RollNo']
rows = []
for _ in range(3):
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")
    rows.append([name, age, roll])
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
print("Student records written to students.csv")
