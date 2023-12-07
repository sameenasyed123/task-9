from functools import reduce

# Number of elements in the Fibonacci series
num_elements = 50

# Using lambda function and reduce to generate Fibonacci series
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 1), [0, 1])

# Generate Fibonacci series with 50 elements
result = fibonacci_series(num_elements)

# Print the result
print(result)
