n = int(input()) # 채널 입력
m = int(input()) # 빠진 버튼 수 입력
if m!=0: # 빠진 버튼이 없다면 입력X
    arr = list(map(int, input().split()))
else:
    arr = []

a = 0
answer = abs(100-n) # 맨 처음 시작 개수 (시작 채널 100)
for channel in range(999999):
    flag = True
    for ch in str(channel):
        if int(ch) in arr:
            flag = False
            break

    if flag:
        a+=1
        size = len(str(channel))
        answer = min(answer, abs(n-channel)+size)

print(answer)