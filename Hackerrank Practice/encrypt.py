# Main Technique [Follow This]
from math import sqrt

s = input()
str_sq = int(sqrt(len(s)))
rows = str_sq if str_sq * str_sq == len(s) else str_sq + 1
for i in range(rows):
    print("".join(s[i] for i in range(i, len(s), rows)), end = ' ')


# Noob Technique -> Don't Follow
'''
import math as m

s = input()
x = ''.join(s.split())
# print(x)
sqr_L = m.sqrt(len(x))
rows, cols = m.floor(sqr_L), m.ceil(sqr_L)
if rows * cols < len(x):
    rows += 1
# print(len(x), sqr_L, rows, cols)
if len(x) != rows * cols:
    x += ((rows * cols) - len(x)) * 'X'
enc = []
ans = []
q = 0
for i in range(rows):
    enc.append(x[q : q + cols])
    # print(x[q : q + cols])
    q += cols
# print(*enc)
for i in range(cols):
    for j in range(rows):
        try:
            ans.append(enc[j][i])
        except:
            ans.append('X')
# print(*ans)
ans = ''.join(ans)#.replace('RB', '')
# print(ans)
# ans = ' '.join([ans[i : i+3] for i in range(len(ans), 3)])
ans = [ans[i:i+3] for i in range(0, len(x), 3)]
# print(*ans)
enc = [i.replace('X', '') for i in ans]
print(*enc)
'''
