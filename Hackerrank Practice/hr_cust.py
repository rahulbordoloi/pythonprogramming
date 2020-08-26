# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

n = int(input())
s_lis = list(map(int, input().split()))
dictx = Counter(s_lis)
n_cust = int(input())
money = 0
for i in range(n_cust):
    x, y = map(int, input().split())
    # print(s_lis, x, y)
    if x in s_lis:
        # print(y)
        if dictx[x] > 0:
            money += y
            dictx[x] -= 1
print(money)
