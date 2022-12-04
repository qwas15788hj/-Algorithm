import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()
s2 = input().strip()
arr = [[0]*5 for _ in range(5)]
alpha = [False]*26 #알파벳 사용했는지 방문처리
alpha[ord("J")-65] = True #J는 없으므로 True

idx = 0 #배열에 넣을 인덱스 번호
for i in s2:
    if not alpha[ord(i)-65]: #해당 알파벳이 사용 안되었으면
        arr[idx//5][idx%5] = i #배열위치에 넣기
        idx += 1 #인덱스 증가
        alpha[ord(i)-65] = True #알파벳 사용 체크

for i in range(5): #배열 돌면서
    for j in range(5):
        if arr[i][j] == 0: #채워지지 않았으면
            for z in range(len(alpha)): #알파벳 돌면서
                if not alpha[z]: #안쓴 안파벳 있다면
                    arr[i][j] = chr(z+65) #해당 알파벳 넣어주고
                    alpha[z] = True #방문체크
                    break

words = []
queue = deque([])
for i in s:
    queue.append(i)
while len(queue) > 1:
    word1 = queue.popleft()
    word2 = queue.popleft()
    if word1 == word2:
        if word1 == "X":
            queue.appendleft(word2)
            queue.appendleft("Q")
            queue.appendleft(word1)
        else:
            queue.appendleft(word2)
            queue.appendleft("X")
            queue.appendleft(word1)
    else:
        words.append([word1, word2])

if queue:
    words.append([queue.popleft(), "X"])

answer = []
for word in words: #단어 돌면서
    target1 = word[0] #첫 단어
    target2 = word[1] #두번째 단어
    target1_x, target1_y = 0, 0 #첫 단어 x, y 값
    target2_x, target2_y = 0, 0 #두번째 단어 x, y 값
    for i in range(5): #배열 돌면서
        for j in range(5):
            if arr[i][j]==target1: #첫 단어랑 같다면 위치 저장
                target1_x = i
                target1_y = j
            if arr[i][j]==target2: #두번째 단어랑 같다면 위치 저장
                target2_x = i
                target2_y = j

    #같은 행에 있다면
    if target1_x == target2_x:
        answer.append(arr[target1_x][(target1_y+1)%5]) #오른쪽 한칸 이동한 값
        answer.append(arr[target2_x][(target2_y+1)%5]) #오른쪽 한칸 이동한 값
    #같은 열에 있다면
    elif target1_y == target2_y:
        answer.append(arr[(target1_x+1)%5][target1_y]) #아래로 한칸 이동한 값
        answer.append(arr[(target2_x+1)%5][target2_y]) #아래로 한칸 이동한 값
    #행, 열 모두 다른 위치면
    else:
        answer.append(arr[target1_x][target2_y]) #내 열, 상대 행
        answer.append(arr[target2_x][target1_y]) #내 열, 상대 행

result = ""
for i in answer:
    result += i
print(result)