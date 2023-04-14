#!/usr/bin/python3
"""function that executes only 
two opreations copy and paste"""


def minOperations(n):
    if n == 1:
        return 0  # If n is already 1, no operations are needed.
    
    operations = 0
    buffer = 1
    
    while buffer < n:
        if n % buffer == 0:
            operations += 2  # Copy all and paste n/buffer times.
            buffer *= n // buffer
        else:
            buffer += 1
            operations += 1
        
        if operations > n:  # If the number of operations exceeds n, return 0.
            return 0
        
    return operations
