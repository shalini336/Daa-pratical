import time


# Linear Search
def linear_search(arr, key):
    # Check each element one by one
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1


# Binary Search
def binary_search(arr, key):
    # Binary search requires a sorted array
    low = 0
    high = len(arr) - 1

    # Continue searching while the range is valid
    while low <= high:
        mid = (low + high) // 2

        # Check if the middle element is the key
        if arr[mid] == key:
            return mid

        # Search in the left half
        elif arr[mid] > key:
            high = mid - 1

        # Search in the right half
        else:
            low = mid + 1

    return -1


# Take input from the user
arr = list(map(int, input("Enter elements separated by space: ").split()))

key = int(input("Enter element to search: "))

print("Array:", arr)
print("Element to search:", key)


# Linear Search
start = time.perf_counter()
result = linear_search(arr, key)
end = time.perf_counter()

print("\nLinear Search")

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(1), Average O(n), Worst O(n)")


# Sort the array before Binary Search
sorted_arr = sorted(arr)


# Binary Search
start = time.perf_counter()
result = binary_search(sorted_arr, key)
end = time.perf_counter()

print("\nBinary Search")
print("Sorted Array:", sorted_arr)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(1), Average O(log n), Worst O(log n)")