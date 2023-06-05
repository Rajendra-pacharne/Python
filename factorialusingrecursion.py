def fact(n):
    if n == 0:  # Base case: if n is 0, return 1 (the factorial of 0 is defined as 1).
        return 1
    else:
        return n * fact(n - 1)  # Recursive case: return n multiplied by the factorial of (n-1).

n = int(input())  # Read an integer input from the user.

# Print the factorial of n by calling the 'fact' function and passing n as an argument.
print("Factorial of", n, ":", fact(n))
