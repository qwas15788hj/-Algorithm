import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split())) #배열 입력
dp = [0]*(n+1) #새로운 배열 생성
for i in range(1, n+1): #새로운 배열 돌면서
    dp[i] = dp[i-1]+arr[i-1] #새로운 배열에 누적합(이전 합 + 현재 값)

for i in range(m):
    start, end = map(int, input().split())
    print(dp[end]-dp[start-1]) #끝점 - (시작점-1)