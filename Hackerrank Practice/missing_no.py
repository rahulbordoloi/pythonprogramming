from collections import Counter
mod = 1000000007
n = int(input())     # Size of the first list
n %= mod
a = list(map(int, input().split())) 
a = [i % mod for i in a]
m = int(input())     # Size of the 2nd list
m %= mod
b = list(map(int, input().split())) 
b = [i % mod for i in b]
# ans = list(set(b) ^ set(a))
c = dict()
for i in a:
    if i not in c:
        c[i] = -1
    else:
        c[i] -= 1
for i in b:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1
ans = []
for i in c:
    if c[i] > 0:
        ans.append(i)
ans.sort()
for i in ans:
    print(i, end =' ')

del a, b, n, m, ans, c
