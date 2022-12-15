n = int(input()) # n입력
m = int(input()) # m입력
s = input() # 문자열 s입력

idx = 0 # 현재 보는 인덱스
count = 0 # IOI 나온 개수
answer = 0 # 정답 개수

while idx < m-2: # 인덱스가 s에서 3개를 확인할 수 있을 때까지
    if s[idx:idx+3] == "IOI": # 현재 인덱스에서 3개가 IOI라면
        count += 1 # 나온 갯수 증가
        idx += 2 # 인덱스 2증가 => 다음에도 IOI 이여야 하기에
        if count == n: # 나온 IOI 개수가 필요한 n과 같다면
            answer += 1 # 정답 증가
            count -= 1 # IOI하나 사용했으므로 -1
    else: # IOI가 아니면
        idx += 1 # 인덱스 1증가
        count = 0 # 나온 IOI 초기화

print(answer)