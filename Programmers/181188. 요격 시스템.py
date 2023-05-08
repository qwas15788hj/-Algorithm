import heapq


def solution(targets):
    answer = 0

    targets.sort()  # 정렬

    arr = []
    heapq.heappush(arr, targets[0][1])  # 우선순위 큐인 힙 이용하여 끝 점 넣기
    answer += 1  # +1

    for i in range(1, len(targets)):  # 타겟 돌면서
        if targets[i][0] < arr[0]:  # 현재 타겟 시작점이 큐의 가장 작은 끝 점보다 작으면
            heapq.heappush(arr, targets[i][1])  # 현재 타겟 끝 점 넣기
        else:  # 현재 타겟 시작점이 큐의 가장 작은 끝 점보다 크면
            arr = []  # 배열 초기화
            heapq.heappush(arr, targets[i][1])  # 현재 타겟 끝 점 넣기
            answer += 1  # +1

    return answer