# Heapify the array
def heapify(arr, n, i):
    # Assume the root is the largest
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check the left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check the right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap if the largest element is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the affected subtree
        heapify(arr, n, largest)


# Max-Heap Sort
def heap_sort(arr):
    a = arr.copy()
    n = len(a)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # Move the largest element to the end
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]

        # Restore the max heap
        heapify(a, i, 0)

    return a


# Take input from the user
arr = list(map(int, input("Enter elements separated by space: ").split()))

print("Original Array:", arr)

# Sort the array
result = heap_sort(arr)

print("Sorted Array:", result)