'''
def updatelist():
    x = ['a', 'b']
    for i in x:
        x.append(i.upper())
        print(x)
updatelist()
'''
'''
x = [3,4,5,-3,100,1,89,54,23,20]
x.sort()
y = []
z = []
for i in range(len(x)):
    if i % 2 == 0:
        y.append(x[i])
    else:
        z.append(x[i])
print(abs(sum(y) - sum(z))) 
print(y)
print(z)
'''
from collections import Counter
tc = int(input())
while tc > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    maxE = max(c, key = c.get)
    # print(maxE)
    if c[maxE] > n//2:  print(maxE) # print(list(c.keys())[list(c.values()).index(maxE)])
    else:   print(-1)
    tc -= 1