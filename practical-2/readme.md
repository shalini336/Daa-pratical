# Practical 2 - Searching Algorithms

## Aim

To implement and analyze Linear Search and Binary Search in Python.

## 1. Linear Search

### Algorithm

1. Start.
2. Read the array and the element to be searched.
3. Start from the first element of the array.
4. Compare the current element with the search element.
5. If both elements are equal, display the position of the element and stop.
6. If they are not equal, move to the next element.
7. Repeat the process until the element is found or the end of the array is reached.
8. If the element is not found, display "Element not found".
9. Stop.

### Time Complexity

- Best Case: O(1)
- Average Case: O(n)
- Worst Case: O(n)

## 2. Binary Search

### Algorithm

1. Start.
2. Read a sorted array and the element to be searched.
3. Set `low` to the first position and `high` to the last position.
4. Find the middle position using `(low + high) // 2`.
5. Compare the middle element with the search element.
6. If they are equal, display the position and stop.
7. If the search element is smaller, search in the left half.
8. If the search element is greater, search in the right half.
9. Repeat until the element is found or `low` becomes greater than `high`.
10. If the element is not found, display "Element not found".
11. Stop.

### Time Complexity

- Best Case: O(1)
- Average Case: O(log n)
- Worst Case: O(log n)
