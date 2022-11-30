import sys
input = sys.stdin.readline

n, m = map(int, input().split())
int_key = dict()
name_key = dict()
for i in range(1, n+1):
    s = input().strip()
    int_key[i] = s
    name_key[s] = i

answer = []
for _ in range(m):
    s = input().strip()
    if s[0].isdigit():
        print(int_key[int(s)])
    else:
        print(name_key[s])