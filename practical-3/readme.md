# Practical 3 - Max Heap Sort

## Aim

To implement the Max-Heap Sort algorithm in Python.

## Algorithm

1. Start.
2. Read the array.
3. Build a max heap from the given array.
4. Compare the parent node with its left and right children.
5. Find the largest element among the parent and its children.
6. If the largest element is not the parent, swap them.
7. Repeat the heapify process until the max heap property is satisfied.
8. Swap the root element with the last element.
9. Reduce the heap size by one.
10. Apply heapify to the remaining heap.
11. Repeat until the array is sorted.
12. Display the sorted array.
13. Stop.