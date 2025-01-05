#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        # Print an empty list when length is 0, as required by the test
        print([])
        return

    # Initialize the Fibonacci sequence
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    # Print the Fibonacci sequence
    print(fibonacci_sequence)