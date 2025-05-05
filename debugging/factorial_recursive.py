#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. It is denoted by n!.
    This implementation uses recursion to compute the factorial.

    Parameters:
        n (int): A non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n (n!).
             For n = 0, returns 1 (0! = 1 by definition).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
