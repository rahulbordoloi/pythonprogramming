'''
Given the time in numerals we may convert it into words, as shown below:

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below. It should return a time string as described.

timeInWords has the following parameter(s):

h: an integer representing hour of the day
m: an integer representing minutes after the hour
Input Format

The first line contains , the hours portion The second line contains , the minutes portion

Constraints

Output Format

Print the time in words as described.

Sample Input 0

5
47
Sample Output 0

thirteen minutes to six
Sample Input 1

3
00
Sample Output 1

three o' clock
Sample Input 2

7
15
Sample Output 2

quarter past seven
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]; 
  
    if (m == 0): 
        return str(nums[h]) + " o' clock" 
  
    elif (m == 1): 
        return "one minute past " + str(nums[h]) 
  
    elif (m == 59): 
        return "one minute to " +  str(nums[(h % 12) + 1]) 
  
    elif (m == 15): 
        return "quarter past " + str(nums[h]) 
  
    elif (m == 30): 
        return "half past " + str(nums[h]) 
  
    elif (m == 45): 
        return "quarter to " + str(nums[(h % 12) + 1]) 
  
    elif (m <= 30): 
        return str(nums[m]) + " minutes past " + str(nums[h]) 
  
    elif (m > 30): 
        return str(nums[60 - m]) + " minutes to " + str(nums[(h % 12) + 1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
