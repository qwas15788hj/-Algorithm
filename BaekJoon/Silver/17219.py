import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
site = dict()

for _ in range(n):
    a, b = map(str, input().strip().split())
    site[a] = b

for _ in range(m):
    s = input().strip()
    print(site[s])