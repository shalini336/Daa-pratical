# Making Change using Dynamic Programming

# Take number of coin denominations
n = int(input("Enter number of coin types: "))

coins = []

# Take coin denominations
for i in range(n):
    coin = int(input(f"Enter coin {i + 1}: "))
    coins.append(coin)

# Take the amount
amount = int(input("Enter amount: "))

# Create DP table
dp = [float('inf')] * (amount + 1)

# 0 coins are needed to make amount 0
dp[0] = 0

# Calculate minimum number of coins
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# Display the result
if dp[amount] == float('inf'):
    print("\nChange cannot be made for the given amount.")
else:
    print("\nMinimum number of coins:", dp[amount])