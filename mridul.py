s = input()
s = s.split()
# print(s)
k = int(input())
c = 0
for i in s:
    z = i[k+1:] + i[:k+1]
    if z == i:
        c += 1
print(c)