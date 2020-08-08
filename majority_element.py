'''
Link -> https://practice.geeksforgeeks.org/problems/majority-element/0

Majority Element 
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:  
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output: 
For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
'''
import time
from collections import Counter

def maj_ele(arr):

    c = Counter(arr)
    maxE = max(c, key = c.get)
    # print(maxE)
    if c[maxE] > n//2:  return maxE # print(list(c.keys())[list(c.values()).index(maxE)])
    else:   return -1

tc = int(input())
while tc > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    
    start = time.time()                                  # Start Time
    print(maj_ele(arr))                                  # Function Call
    end = time.time()                                    # End Time
    print(f"Execution Time : {round((end-start), 8)} s") # Execution Time

    tc -= 1