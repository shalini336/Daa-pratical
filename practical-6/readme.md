# Practical 6 - Chain Matrix Multiplication

## Aim

To implement Chain Matrix Multiplication using Dynamic Programming in Python.

## Algorithm

1. Start.
2. Read the number of matrices.
3. Read `n + 1` dimensions of the matrices.
4. Create a DP table to store the minimum multiplication cost.
5. Set the cost of multiplying a single matrix to 0.
6. Consider matrix chains of increasing length.
7. For each chain, try every possible position to split the chain.
8. Calculate the multiplication cost for each possible split.
9. Select the minimum cost.
10. Store the minimum cost in the DP table.
11. Repeat until the complete matrix chain is processed.
12. The final DP table value gives the minimum number of scalar multiplications.
13. Display the minimum multiplication cost.
14. Stop.

## Time Complexity

- O(n³)

## Space Complexity

- O(n²)

## Input Format

For `n` matrices, enter `n + 1` dimensions separated by spaces.

### Example

For 3 matrices:

```text
Enter number of matrices: 3
Enter 4 dimensions separated by space: 10 20 30 40