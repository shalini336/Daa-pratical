# Matrix Chain Multiplication using Dynamic Programming

# Take the number of matrices
n = int(input("Enter number of matrices: "))

# Take n + 1 dimensions
dimensions = list(
    map(int, input(f"Enter {n + 1} dimensions separated by space: ").split())
)

# Create DP table
dp = [[0 for _ in range(n)] for _ in range(n)]

# Calculate minimum multiplication cost
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1

        dp[i][j] = float('inf')

        # Try all possible positions to split the matrix chain
        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
            )

            # Store the minimum cost
            if cost < dp[i][j]:
                dp[i][j] = cost

# Display the result
print("\nMinimum number of scalar multiplications:", dp[0][n - 1])