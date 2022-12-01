t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    prev = [i for i in range(1, n+1)]
    now = [0]*n
    for i in range(k):
        for j in range(1, n):
            prev[j] += prev[j-1]

    print(prev[n-1])