'''
The median of a list of numbers is essentially it's middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, can you find the median?

For example, the median of  is , the middle element in the sorted array.

Function Description

Complete the findMedian function in the editor below. It must return an integer that represents the median of the array.

findMedian has the following parameter(s):

arr: an unsorted array of integers
Input Format

The first line contains the integer , the size of . 
The second line contains  space-separated integers 

Constraints

 is odd
Output Format

Output one integer, the median.

Sample Input 0

7
0 1 2 4 6 5 3
Sample Output 0

3
Explanation 0

The sorted . It's middle element is at .
'''

#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy as np

# Complete the findMedian function below.
def findMedian(arr):
    # return np.median(arr)
    
    arr.sort()
    return arr[len(arr)//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
