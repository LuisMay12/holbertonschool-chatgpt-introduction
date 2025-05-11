#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer recursively.

    Parameters:
    n (int): The non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the integer argument from the command line, compute factorial and print it
f = factorial(int(sys.argv[1]))
print(f)
