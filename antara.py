s = input()
y = int(input())
n = int(input())
c = 0
for i in s:
    if int(i) <= y:
        c += 1
for i in range(n):
    for j in range(2, n-1):
        if int(s[i:j+i]) <= y:
            c += 1
print(c)

'''
qx = [i for i in range(input1)]
for i, j in input3:
    if i == 1:
        qx = qx[1:]
    if i == 2:
        qx.remove(j)
    if i == 3:
        return qx.index(j)
'''