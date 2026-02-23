# 2. Constructor for Student (already included in 1_student_class.py)
# 3. Single inheritance example
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Person Name: {self.name}")

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

if __name__ == "__main__":
    s = Student("Bob", 85)
    s.display()
    p = Person("Charlie")
    p.display()