#!/usr/bin/python3
"""
Calculates the least number of operations needed
to result in exactly n H characters in the file.
"""

def min0perations(n):
    """
    Returns the fewest number of operations needed to
    output in exactly n H characters in th file
    """

    if n <= 1:
        return 0

    min_ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            min_ops += divisor
            n //= divisor
        divisor += 1

    return min_ops

