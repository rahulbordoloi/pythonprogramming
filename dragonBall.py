from collections import Counter

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        x = int(input())
        balls = list(map(int, input().split()))
        count = Counter(balls)
        balls = list(filter((x).__ne__, balls))
        if balls[0] == count[balls[0]]:
            print("YES")
        else:
            print("NO")
        tc -= 1
