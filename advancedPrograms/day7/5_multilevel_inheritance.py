# 6. Multilevel inheritance example
class Grandparent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Grandparent: {self.name}")

class Parent(Grandparent):
    def __init__(self, name, parent_name):
        super().__init__(name)
        self.parent_name = parent_name

    def show(self):
        print(f"Parent: {self.parent_name}, Grandparent: {self.name}")

class Child(Parent):
    def __init__(self, name, parent_name, child_name):
        super().__init__(name, parent_name)
        self.child_name = child_name

    def show(self):
        print(f"Child: {self.child_name}, Parent: {self.parent_name}, Grandparent: {self.name}")

if __name__ == "__main__":
    c = Child("John Sr.", "John Jr.", "Johnny")
    c.show()