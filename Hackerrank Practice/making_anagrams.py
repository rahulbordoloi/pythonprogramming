#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a1 = list(a)
    b1 = list(b)
    """a1.sort()
    b1.sort()"""
    #anagram=0
    if len(a1)<len(b1):
        a1,b1=b1,a1
    n=len(a1)
    i=0
    while i<n:
        print(i)
        print(n)
        if a1[i] in b1:
            c=a1[i]
            b1.remove(c)
            a1.remove(c)
            n=n-1
            i=i-1
        i+=1
    return len(a1)+len(b1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
