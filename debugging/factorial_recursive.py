#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer.

    Parameters:
    - n: Non-negative integer for which factorial will be calculated.

    Returns:
    - Returns the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
