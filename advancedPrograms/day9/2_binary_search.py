# Binary Search implementation

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
    target = int(input("Enter element to search: "))
    result = binary_search(arr, target)
    print(f"Element found at index: {result}" if result != -1 else "Element not found.")
