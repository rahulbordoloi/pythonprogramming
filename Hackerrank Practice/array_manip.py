# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true

def reduce_x(a, b, c):
    mod = 1000000007
    return a % mod, b % mod, c % mod

# Main Method
if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = [0] * (n + 2)

    for _ in range(m):
        a, b, k = map(int, input().split())
        a, b, k = reduce_x(a, b, k)
        arr[a] += k
        arr[b + 1] -= k
        
        '''
        if a == b:      
            arr[a-1] += k
        else:       
            arr[a-1 : b] = [i + k for i in arr[a-1 : b]]
        '''

    m = v = 0
    for i in range(1, n + 1):
        v += arr[i]
        m = max(m, v)
    print(m)