#!/bin/python3

import math
import os
import random
import re
import sys

def avg(*nums):
    x = len(nums)
    average = float(sum(nums)/x)
    return average


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
