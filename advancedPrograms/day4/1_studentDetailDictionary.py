# this is how we declare a dictionary
student_details = {}

student_details['name'] = input("Enter the student's name: ")
student_details['age'] = int(input("Enter the student's age: "))
student_details['dept'] = input("Enter the student'd department: ")

print("Keys:")
for key in student_details.keys():
    print(key)

print("\nValues")
for value in student_details.values():
    print(value)