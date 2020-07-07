'''
You are given a function . You are also given  lists. The  list consists of elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

%

 denotes the element picked from the  list . Find the maximized value obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and . 
The next  lines each contains an integer , denoting the number of elements in the list, followed by  space separated integers denoting the elements in the list.

Constraints

 
 
 

Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum value equal to % = .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

(K, N) = map(int, input().strip().split(' '))

L = list()
for i in range(K):
    l = list(map(int, input().strip().split(' ')))
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n

S_max = 0
L_max = None

for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print(S_max)