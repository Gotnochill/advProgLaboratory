# 5. Operator overloading for + (add marks of two students)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

if __name__ == "__main__":
    s1 = Student("Alice", 90)
    s2 = Student("Bob", 85)
    print("Total Marks:", s1 + s2)