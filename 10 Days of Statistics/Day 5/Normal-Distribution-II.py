'''
Objective
In this challenge, we go further with normal distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.
Task
The final grades for a Physics exam taken by a large group of students have a mean of  and a standard deviation of . If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
Scored higher than  (i.e., have a )?
Passed the test (i.e., have a )?
Failed the test (i.e., have a )?
Find and print the answer to each question on a new line, rounded to a scale of  decimal places.
Input Format
There are  lines of input (shown below):
70 10
80
60
The first line contains  space-separated values denoting the respective mean and standard deviation for the exam. The second line contains the number associated with question . The third line contains the pass/fail threshold number associated with questions  and .
If you do not wish to read this information from stdin, you can hard-code it into your program.
Output Format
There are three lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):
On the first line, print the answer to question  (i.e., the percentage of students having ).
On the second line, print the answer to question  (i.e., the percentage of students having ).
On the third line, print the answer to question  (i.e., the percentage of students having ).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
val_first_question = float(input())
val_sec_third_question = float(input())

print (round(100 - (cumulative(mean, std, val_first_question) * 100), 2))
print (round(100 - (cumulative(mean, std, val_sec_third_question) * 100), 2))
print (round(cumulative(mean, std, val_sec_third_question) * 100, 2))
