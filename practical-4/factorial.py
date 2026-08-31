import time


# Iterative factorial
def factorial_iterative(n):
    result = 1

    # Calculate factorial using a loop
    for i in range(1, n + 1):
        result *= i

    return result


# Recursive factorial
def factorial_recursive(n):
    # Base condition
    if n == 0 or n == 1:
        return 1

    # Calculate factorial using recursion
    return n * factorial_recursive(n - 1)


# Take input from the user
n = int(input("Enter a number: "))


# Iterative method
start = time.perf_counter()
result1 = factorial_iterative(n)
end = time.perf_counter()

print("\nIterative Method")
print("Factorial:", result1)
print("Execution Time:", format(end - start, ".8f"), "seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Recursive method
start = time.perf_counter()
result2 = factorial_recursive(n)
end = time.perf_counter()

print("\nRecursive Method")
print("Factorial:", result2)
print("Execution Time:", format(end - start, ".8f"), "seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")