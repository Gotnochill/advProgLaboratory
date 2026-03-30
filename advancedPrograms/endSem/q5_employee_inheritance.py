class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

emp = Employee("Alice", "E101")
print(f"Employee Name: {emp.name}, ID: {emp.emp_id}")
