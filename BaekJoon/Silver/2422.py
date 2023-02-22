import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

answer = 0
arr = [i for i in range(n)]
com = list(combinations(arr, 3))
for i in range(len(com)):
    if ice[com[i][0]][com[i][1]] or ice[com[i][0]][com[i][2]] or ice[com[i][1]][com[i][2]]:
        continue
    answer += 1

print(answer)