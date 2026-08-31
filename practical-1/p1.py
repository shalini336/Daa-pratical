import time

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()

    # Compare adjacent elements and swap them
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# Selection Sort
def selection_sort(arr):
    a = arr.copy()

    # Find the smallest element and place it at the correct position
    for i in range(len(a) - 1):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()

    # Insert each element into its correct position
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# Merge Sort
def merge_sort(arr):
    # An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr.copy()

    # Divide the array into two parts
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Merge two sorted arrays
def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
def quick_sort(arr):
    # An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr.copy()

    # Select the last element as pivot
    pivot = arr[-1]

    left = []
    right = []

    # Divide elements around the pivot
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Take input from the user
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

# Bubble Sort
start = time.perf_counter()
result = bubble_sort(arr)
end = time.perf_counter()

print("\nBubble Sort")
print("Sorted Array:", result)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(n), Average O(n²), Worst O(n²)")


# Selection Sort
start = time.perf_counter()
result = selection_sort(arr)
end = time.perf_counter()

print("\nSelection Sort")
print("Sorted Array:", result)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(n²), Average O(n²), Worst O(n²)")


# Insertion Sort
start = time.perf_counter()
result = insertion_sort(arr)
end = time.perf_counter()

print("\nInsertion Sort")
print("Sorted Array:", result)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(n), Average O(n²), Worst O(n²)")


# Merge Sort
start = time.perf_counter()
result = merge_sort(arr)
end = time.perf_counter()

print("\nMerge Sort")
print("Sorted Array:", result)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(n log n), Average O(n log n), Worst O(n log n)")


# Quick Sort
start = time.perf_counter()
result = quick_sort(arr)
end = time.perf_counter()

print("\nQuick Sort")
print("Sorted Array:", result)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best O(n log n), Average O(n log n), Worst O(n²)")