# Saurav Codevita Solution
# Fill the Cube

import time
import math

def find_cube(n):

    l, c = [], 0

    for i in range(n):
        l.append(list(map(str, input().split())))
    for j in range(n):
        for k in range(n):
            if l[j][k] == 'D':
                c += 1
    return math.floor(math.sqrt(c))


if __name__ == '__main__':

    n = int(input())

    start = time.time()                                  # Start Time
    print(find_cube(n))                                  # Function Call
    end = time.time()                                    # End Time
    print(f"Execution Time : {round((end-start), 8)} ms") # Execution Time
    