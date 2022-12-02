import heapq, sys
input = sys.stdin.readline

t = int(input()) #테스트 수
for _ in range(t):
    k = int(input()) #연산 횟수
    min_heap = [] #최소힙
    max_heap = [] #최대힙
    visited = [False]*1000001
    for key in range(k):
        command, num = map(str, input().strip().split())
        num = int(num)
        if command=="I":
            heapq.heappush(min_heap, (num, key)) #어떤 원소를 뺏는지 key값 넣어주기
            heapq.heappush(max_heap, (-num, key))
            visited[key] = True #뺄 수 있는 key값 추가
        else:
            if num==-1: #최소힙에서 빼기
                while min_heap and not visited[min_heap[0][1]]: #최소힙의 원소가 남아있고, 방문했다면(이미 뺀값이면)
                    heapq.heappop(min_heap)
                if min_heap: #최소힙이 남아있고, 뺄 수 있다면
                    visited[min_heap[0][1]] = False #최소힙에서 뺄 수 있으니 방문처리하고
                    heapq.heappop(min_heap) #빼주기
            else: #최대힙에서 빼기
                while max_heap and not visited[max_heap[0][1]]: #최대힙의 원소가 남아있고, 방문했다면(이미 뺀값이면)
                    heapq.heappop(max_heap)
                if max_heap: #최대힙이 남아있고, 뺄 수 있다면
                    visited[max_heap[0][1]] = False #최대힙에서 뺄 수 있으니 방문처리하고
                    heapq.heappop(max_heap) #빼주기

        #방문한 값 한번 더 확인해주기
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")