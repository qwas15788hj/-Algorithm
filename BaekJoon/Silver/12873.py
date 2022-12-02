import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #입력받기
queue = deque([]) #큐 생성
for i in range(1, n+1): #큐에 저장
    queue.append(i)

turn = 0 #현재 턴
while len(queue)!=1: #큐의 개수가 1개가 될 때까지
    turn += 1 #현재 턴+1
    count = turn**3 #몇 번 세야하는지(현재 턴의 세제곱)
    number = count%len(queue) #빼야하는 번호 구하기(횟 수%큐 갯수)
    idx = (len(queue)-1+number)%len(queue) #빼야하는 번호의 인덱스 구하기((큐 개수-1+현재 번호)%큐 개수)
    for _ in range(idx): #빼야하는 수만큼 돌면서
        queue.append(queue.popleft()) #앞에 숫자 뒤로 이동
    queue.popleft() #앞에 숫자 빼기

print(queue[0])