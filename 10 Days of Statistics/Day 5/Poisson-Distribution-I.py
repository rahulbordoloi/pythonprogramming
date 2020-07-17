'''
Objective
In this challenge, we learn about Poisson distributions. Check out the Tutorial tab for learning materials!

Task
A random variable, , follows Poisson distribution with mean of . Find the probability with which the random variable  is equal to .

Input Format

The first line contains 's mean. The second line contains the value we want the probability for:

2.5
5
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

mean = float(input())
k = float(input())
e = 2.71828

result = ((mean ** k) * (e ** -mean)) /  factorial(k)
print(round(result, 3))
