import sys
input = sys.stdin.readline

left = list(input().strip()) # 문자열 리스트로 입력 => 커서가 맨 오른쪽임으로 left로 저장
m = int(input().strip()) # 명령어 개수 입력
right = [] # 커서 오른쪽

# append(), pop() 시간 복잡도 : O(1)
# insert()        시간 복잡도 : O(N)
# 이 문제는 시간을 줄이기 위해 append와 pop을 사용해야함
# insert 사용시 시간초과

for _ in range(m): # 명령어만큼 반복
    command = list(map(str, input().strip().split())) # 명령어 입력
    if command[0] == "L": # 명령어 시작이 L이면
        if len(left) != 0: # 왼쪽 배열이 빈 배열이 아니면
            right.append(left.pop()) # 왼쪽 끝을 오른쪽 끝으로 이동
    elif command[0] == "D": # 명령어 시작이 D이면
        if len(right) != 0: # 오른쪽 배열이 빈 배열이 아니면
            left.append(right.pop()) # 오른쪽 끝을 왼쪽 끝으로 이동
    elif command[0] == "B": # 명령어 시작이 B이면
        if len(left) != 0: # 왼쪽이 빈 배열이 아니면
            left.pop() # 빼주기
    else: # 명령어 시작이 P이면
        left.append(command[1]) # 왼쪽 배열에 단어 추가

print("".join(left) + "".join(right[::-1])) # 왼쪽 배열 + 오른쪽 배열(거꾸로)