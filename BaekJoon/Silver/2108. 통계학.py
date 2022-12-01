import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(round(sum(arr)/n))

arr.sort()
print(arr[n//2])

val = Counter(arr).most_common()
if len(val) > 1:
    if val[0][1] == val[1][1]:
        print(max(val[0][0], val[1][0]))
    else:
        print(val[0][0])
else:
    print(val[0][0])

print(arr[-1]-arr[0])