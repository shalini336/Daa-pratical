# Practical 4 - Factorial

## Aim

To implement and analyze the factorial program using iterative and recursive methods in Python.

## 1. Iterative Method

### Algorithm

1. Start.
2. Read the value of `n`.
3. Set `result = 1`.
4. Repeat from 1 to `n`.
5. Multiply `result` by the current value of `i`.
6. Store the result.
7. Display the factorial.
8. Stop.

### Time Complexity

- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

### Space Complexity

- O(1)

## 2. Recursive Method

### Algorithm

1. Start.
2. Read the value of `n`.
3. Check if `n` is 0 or 1.
4. If `n` is 0 or 1, return 1.
5. Otherwise, multiply `n` by the factorial of `n - 1`.
6. Continue the recursive calls until the base condition is reached.
7. Return the calculated factorial.
8. Display the factorial.
9. Stop.

### Time Complexity

- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)

### Space Complexity

- O(n)
