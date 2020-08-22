# Saurav Codevita Solution
# Even Odd Problem

import time
from itertools import product

mod = 1000000007

def sum_group(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s

if __name__ == '__main__':

    low, high = map(int, input().split())
    g = int(input())
    lst = []

    start = time.time()                                 # Start Time

    for i in range(low, high + 1):
        lst.append(str(i))

    c = 0
    perm = product(lst, repeat = g)
    for i in perm:
        if (sum_group(i) % 2 == 0):
            c += 1

    end = time.time()                                    # End Time

    print(c % mod)

    print(f"Execution Time : {round((end-start), 8)} s") # Execution Time