n = int(input())                            # 1
k = int(input())                            # 2
x = int(input())                            # 3
y = int(input())                            # 4
arr = list(map(int, input().split()))       # 5

# s = sum(arr[:k+1])
w = 50

if k != 1:
    for i in range(n):
        arr[i] = sum(arr[i:i+k])
    arr = arr[:-1]

# print(arr, len(arr))

for i in arr:
    # print(i)
    if i in range(x, y + 1):    w = w
    elif i < x:     w -= 1
    elif i > y:     w += 1

print(w-50)