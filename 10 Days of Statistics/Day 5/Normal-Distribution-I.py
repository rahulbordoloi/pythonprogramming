'''
Objective
In this challenge, we learn about normal distributions. Check out the Tutorial tab for learning materials!
Task
In a certain plant, the time taken to assemble a car is a random variable, , having a normal distribution with a mean of  hours and a standard deviation of  hours. What is the probability that a car can be assembled at this plant in:
Less than  hours?
Between  and  hours?
Input Format
There are  lines of input (shown below):
20 2
19.5
20 22
The first line contains  space-separated values denoting the respective mean and standard deviation for . The second line contains the number associated with question . The third line contains  space-separated values describing the respective lower and upper range boundaries for question .
If you do not wish to read this information from stdin, you can hard-code it into your program.
Output Format
There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):
On the first line, print the answer to question  (i.e., the probability that a car can be assembled in less than  hours).
On the second line, print the answer to question  (i.e., the probability that a car can be assembled in between  to  hours).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

print (round(cumulative(mean, std, less_period),3))
print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))
