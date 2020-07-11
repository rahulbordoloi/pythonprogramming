'''
Objective 
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task 
The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).

Input Format

A single line containing the following values:

1.09 1
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e., format).
'''

'''
from stats import Stats

boysWeight = 1.09
girlsWeight = 1.0
probBoy = boysWeight / (boysWeight + girlsWeight)

print(round(1-Stats.binomDistCumulative(2,6,probBoy), 3))
'''

pp=str(input())
p1=float(pp[:pp.find(' ')])
p2=float(pp[pp.find(' ')+1:])
pf=0.0

p = p1/(p1+p2)
from math import factorial as f
def comb(n,r):
    return f(n) / f(r) / f(n-r)


for i1 in range(3,7):
    prob_i1 = pow(p,i1)*pow(1-p,6-i1)*comb(6,i1)
    pf += prob_i1
print("%.3f"%(pf))  # == round(x,3)
