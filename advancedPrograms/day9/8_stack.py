# Stack implementation using list

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = Stack()
    while True:
        print("\nChoose operation: push, pop, peek, is_empty, size, show, exit")
        op = input("Operation: ").strip().lower()
        if op == "push":
            item = input("Enter item to push: ")
            s.push(item)
        elif op == "pop":
            print("Popped:", s.pop())
        elif op == "peek":
            print("Peek:", s.peek())
        elif op == "is_empty":
            print("Is Empty:", s.is_empty())
        elif op == "size":
            print("Size:", s.size())
        elif op == "show":
            print("Stack:", s.stack)
        elif op == "exit":
            break
        else:
            print("Invalid operation.")
