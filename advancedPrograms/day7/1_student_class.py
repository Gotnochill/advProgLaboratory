# 1. Student class with display method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Example usage
if __name__ == "__main__":
    s = Student("Alice", 90)
    s.display()