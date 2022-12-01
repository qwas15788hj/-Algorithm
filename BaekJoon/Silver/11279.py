import heapq, sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h)*-1)
    else:
        heapq.heappush(h, -1*x)