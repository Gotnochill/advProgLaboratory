# 4. Method overriding demonstration
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

if __name__ == "__main__":
    a = Animal()
    a.speak()
    d = Dog()
    d.speak()