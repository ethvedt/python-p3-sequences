#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq = []
    if length > 0:
        for i in range(length):
            if i == 0:
                fib_seq.append(0)
            elif i == 1:
                fib_seq.append(1)
            else:
                new_fib = fib_seq[-2] + fib_seq[-1]
                fib_seq.append(new_fib)
    print(fib_seq)