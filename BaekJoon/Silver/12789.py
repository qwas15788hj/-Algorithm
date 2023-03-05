from collections import deque

n = int(input()) # 개수 입력
queue = deque(list(map(int, input().split()))) # 줄서있는 순서
stack = deque() # 쉴 수 있는 공간
target = 1 # 현재 줘야하는 번호
cnt = 0 # 몇명받았는지
while queue: # 모든 사람이 다 받을 때까지
    if queue and queue[0] == target: # 서있는 사람이 있고 맨 앞이 현재 받을 사람일때
        queue.popleft() # 꺼내고
        target += 1 # 번호 + 1
        cnt += 1 # 카운트 + 1
    else: # 서있는 사람이 없거나 현재 받을 사람이 아니면
        stack.append(queue.popleft()) # 쉬는 공간에 추가
    while stack and stack[-1] == target: # 쉬는 공간에 사람이 있고 맨뒤가 받을 사람일때
        stack.pop() # 꺼내고
        target += 1 # 번호 + 1
        cnt += 1 # 카운트 + 1

if cnt == n: # 모든 사람이 다 받았을 때
    print("Nice")
else:
    print("Sad")