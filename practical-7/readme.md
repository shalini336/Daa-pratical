# Practical 7 - Making Change using Dynamic Programming

## Aim

To implement the Making Change problem using Dynamic Programming in Python.

## Algorithm

1. Start.
2. Read the number of coin types.
3. Read the value of each coin.
4. Read the amount for which change is required.
5. Create a DP array of size `amount + 1`.
6. Initialize all values with infinity.
7. Set `dp[0] = 0` because zero coins are needed to make amount 0.
8. For each amount from 1 to the given amount:
   - Check every available coin.
   - If the coin value is less than or equal to the current amount, calculate the number of coins required.
   - Store the minimum number of coins.
9. Check the value of `dp[amount]`.
10. If it is infinity, display that change cannot be made.
11. Otherwise, display the minimum number of coins required.
12. Stop.

## Time Complexity

- O(n × A)

Where:
- `n` = number of coin types
- `A` = amount
