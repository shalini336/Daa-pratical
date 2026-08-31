# 0/1 Knapsack using Dynamic Programming

# Take number of items
n = int(input("Enter number of items: "))

weights = []
values = []

# Take weight and value of each item
for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

# Take maximum capacity
capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # Check if the item can fit
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Find the selected items
w = capacity
selected_items = []

for i in range(n, 0, -1):
    # Check whether item i was selected
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= weights[i - 1]

# Reverse the list to show items in original order
selected_items.reverse()

# Calculate total weight
total_weight = sum(weights[i - 1] for i in selected_items)

# Display the result
print("\nMaximum value:", dp[n][capacity])
print("Selected items:", selected_items)
print("Total weight:", total_weight)
print("Total value:", dp[n][capacity])