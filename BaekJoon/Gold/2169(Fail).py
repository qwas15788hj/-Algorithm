import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)] # 누적합
for i in range(n):
    for j in range(m):
        if j==0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = dp[i][j-1] + arr[i][j]

answer = [[0]*m for _ in range(n)]
for i in range(m):
    answer[0][i] = dp[0][i]

for i in range(1, n): # 총 1~n줄 까지
    for j in range(m): #총 0~m까지
        answer[i][j] = -1e9
        for k in range(m): # m가지 방법
            if k < j:
                if k-1 < 0:
                    answer[i][j] = max(answer[i][j], answer[i-1][k]+dp[i][j])
                else:
                    answer[i][j] = max(answer[i][j], answer[i-1][k]+dp[i][j]-dp[i][k-1])
            elif k==j:
                answer[i][j] = max(answer[i][j], answer[i-1][k]+arr[i][j])
            else:
                if j-1 < 0:
                    answer[i][j] = max(answer[i][j], answer[i-1][k]+dp[i][k])
                else:
                    answer[i][j] = max(answer[i][j], answer[i-1][k]+dp[i][k]-dp[i][j-1])

# print(dp)
# print(answer)
print(answer[n-1][m-1])