# Practical 1 - Sorting Algorithms

## Aim

To implement and analyze the following sorting algorithms in Python:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort

## 1. Bubble Sort

### Algorithm

1. Start.
2. Read the array.
3. Compare adjacent elements.
4. If the first element is greater than the second element, swap them.
5. Continue comparing adjacent elements until the end of the array.
6. Repeat the process for all elements until the array is sorted.
7. Display the sorted array.
8. Stop.

### Time Complexity

- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

## 2. Selection Sort

### Algorithm

1. Start.
2. Read the array.
3. Find the smallest element in the array.
4. Swap it with the first element.
5. Find the smallest element from the remaining unsorted elements.
6. Swap it with the next element.
7. Repeat until the entire array is sorted.
8. Display the sorted array.
9. Stop.

### Time Complexity

- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)

## 3. Insertion Sort

### Algorithm

1. Start.
2. Read the array.
3. Consider the first element as sorted.
4. Select the next element as the key.
5. Compare the key with the elements before it.
6. Shift elements greater than the key one position to the right.
7. Insert the key into its correct position.
8. Repeat until all elements are sorted.
9. Display the sorted array.
10. Stop.

### Time Complexity

- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

## 4. Merge Sort

### Algorithm

1. Start.
2. Read the array.
3. Divide the array into two halves.
4. Recursively divide each half until each part contains one element.
5. Compare the elements of the two parts.
6. Merge the elements in sorted order.
7. Continue merging until the complete array is sorted.
8. Display the sorted array.
9. Stop.

### Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

## 5. Quick Sort

### Algorithm

1. Start.
2. Read the array.
3. Select an element as the pivot.
4. Divide the remaining elements into two groups:
   - Elements smaller than or equal to the pivot.
   - Elements greater than the pivot.
5. Recursively apply Quick Sort to both groups.
6. Combine the left group, pivot, and right group.
7. Display the sorted array.
8. Stop.

### Time Complexity

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

## Time Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case |

| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |