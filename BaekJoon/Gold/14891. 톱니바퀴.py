from collections import deque

gear = []
for _ in range(4):
    queue = deque()
    a = input()
    for i in range(len(a)):
        queue.append(int(a[i]))
    gear.append(queue)

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1
    rotate = [0]*4
    rotate[num] = dir # 회전 정보 저장할 배열

    # 왼쪽
    pre_left = gear[num][6]
    for i in range(num-1, -1, -1): # 선택 기어 전부터 0까지
        now_left = gear[i][6]
        now_right = gear[i][2]

        if pre_left==now_right:
            break
        else:
            pre_left = now_left
            rotate[i] = rotate[i+1]*-1 # 앞의 회전 정보*-1

    #오른쪽
    pre_right = gear[num][2]
    for i in range(num+1, 4): # 선택 기어 이후부터 3까지
        now_left = gear[i][6]
        now_right = gear[i][2]

        if pre_right==now_left:
            break
        else:
            pre_right = now_right
            rotate[i] = rotate[i-1]*-1

    for i in range(4):
        gear[i].rotate(rotate[i]) # 저장된 회전 정보에 따라 회전

answer = 0
for i in range(4):
    if gear[i][0]==1:
        answer += int(2**i)

print(answer)