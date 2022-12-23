import sys
input = sys.stdin.readline
from collections import deque

t = int(input()) # 테스트케이스 t 입력

def bfs(start): # 명령어 찾기 위한 bfs 함수
    queue = deque([]) # 큐 생성
    queue.append(start) # 큐에 시작 값 넣기
    visited[start] = "T" # 맨 처음 시작 단어 방문체크해야함!!! 안하면 오답
    while queue: # 큐가 빌때까지
        size = len(queue) # 큐 크기
        for i in range(size): # 큐 크기만큼 반복
            x = queue.popleft() # 현재 값 큐에서 빼기
            if x == b: # 현재 값이 b와 같다면
                break # 끝

            nx = (2*x)%10000 # D 명령어를 이용한 값 nx
            if not visited[nx]: # 방문 안했다면
                queue.append(nx) # 큐에 넣고
                visited[nx] = visited[x] + "D" # 이전 명령어 + D

            nx = x-1 # S 명령어를 이용한 값 nx
            if nx == -1: # nx가 -1 이면
                nx = 9999 # 9999로 갱신
            if not visited[nx]: # 방문 안했다면
                queue.append(nx) # 큐에 넣고
                visited[nx] = visited[x] + "S" # 이전 명령어 + S

            nx_l = str(x) # L 명령어 사용하기 위해 현재 값 x를 문자열로 바꾸기
            if len(nx_l) != 4: # 문자열의 길이가 4가 아니면
                nx_l = "0"*(4-len(nx_l)) + nx_l # 앞에 부족한 수 만큼 0붙이기
            nx_l = nx_l[1:len(nx_l)] + nx_l[0] # L 명령어 사용한 값 1~4번째 + 0번째
            nx = int(nx_l) # 문자열 nx_l을 숫자로
            if not visited[nx]: # 방문 안했다면
                queue.append(nx) # 큐에 넣고
                visited[nx] = visited[x] + "L" # 이전 명령어 + L

            nx_r = str(x) # R 명령어 사용하기 위해 현재 값 x를 문자열로 바꾸기
            if len(nx_r) != 4: # 문자열의 길이가 4가 아니면
                nx_r = "0"*(4-len(nx_r)) + nx_r # 앞에 부족한 수 만큼 0붙이기
            nx_r = nx_r[3] + nx_r[0:3] # R 명령어 사용한 값 마지막 4번째 + 0~3번째
            nx = int(nx_r) # 문자열 nx_r을 숫자로
            if not visited[nx]: # 방문 안했다면
                queue.append(nx) # 큐에 넣고
                visited[nx] = visited[x] + "R" # 이전 명령어 + R

for _ in range(t): # 테스트케이스 반복
    a, b = map(int, input().split()) # a, b 입력
    visited = [""]*10000 # 방문처리 및 명령어 저장할 10000개의 빈 문자열 배열 생성
    bfs(a) # bfs 함수 호출
    print(visited[b][1:]) # b가 되기 위한 명령어가 들어있는 visited[b] 중 맨 처음 방문처리를 위한 0번째 인덱스 제거 후 출력