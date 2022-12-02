n = int(input())
arr = [0]*1001
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
    arr[i] = arr[i-2]+arr[i-1]

print(arr[n]%10007)
# 길이가 i 일때
# i-1에서 1*2타일 세워서 놓는 방법 1가지
#           +
# i-2일때 2*1타일 2개를 눕히는 방법, (1*2타일 2개를 세우는 방법 (i-1일때와 겹쳐서X))