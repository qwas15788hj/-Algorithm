def solution(k, d):
    answer = 0
    # x 축 기준
    for i in range(0, d + 1, k):  # 0~d까지 k 증가
        y = (pow(d, 2) - pow(i, 2)) ** 0.5  # y축 : 총거리-x거리 ** 0.5
        answer += y // k + 1  # y축도 k만큼 증가 + 0일때 1

    return answer