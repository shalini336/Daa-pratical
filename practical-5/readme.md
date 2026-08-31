# Practical 5 - 0/1 Knapsack using Dynamic Programming

## Aim

To implement the 0/1 Knapsack problem using Dynamic Programming in Python and find the selected items that give the maximum value.

## Algorithm

1. Start.
2. Read the number of items.
3. Read the weight and value of each item.
4. Read the maximum capacity of the knapsack.
5. Create a DP table with rows representing items and columns representing capacities.
6. Initialize all values in the table to 0.
7. For each item, check whether its weight is less than or equal to the current capacity.
8. If the item can fit, calculate the maximum of:
   - Value obtained by including the item.
   - Value obtained by excluding the item.
9. If the item cannot fit, use the value from the previous row.
10. Continue until all items and capacities are processed.
11. The last cell of the DP table contains the maximum value.
12. Trace the DP table backwards to find the selected items.
13. Calculate the total weight of the selected items.
14. Display the maximum value, selected items, and total weight.
15. Stop.

## Time Complexity

- O(n × W)

Where:
- `n` = number of items
- `W` = capacity of the knapsack

