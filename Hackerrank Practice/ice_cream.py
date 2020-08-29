tc = int(input())
for _ in range(tc):

    m = int(input())
    n = int(input())
    costs = [int(i) for i in input().split()]
    flag = 0
    for i in range(n):
        for j in range(i+1, n):
            if costs[i] + costs[j] == m:
                print(str(i+1) + ' ' + str(j+1))
                flag = 1
                break
        if flag:
            break