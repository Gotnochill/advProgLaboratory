# Linear Search implementation

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    target = int(input("Enter element to search: "))
    result = linear_search(arr, target)
    print(f"Element found at index: {result}" if result != -1 else "Element not found.")
