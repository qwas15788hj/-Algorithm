import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = [] #최소힙
    max_heap = [] #최대힙
    visited = [False]*1000001 #방문체크
    for key in range(k):
        command, num = map(str, input().strip().split()) #입력
        num = int(num) #숫자로
        if command=="I": #I면
            heapq.heappush(min_heap, (num, key)) #최소힙에 key값 들고 넣기
            heapq.heappush(max_heap, (-num, key)) #최대힙에 key값 들고 넣기
            visited[key] = True #key값 사용 가능 표시
        else:
            if num==-1:
                while min_heap and not visited[min_heap[0][1]]: #최소힙이 남아있고, 삭제 불가능하면
                    heapq.heappop(min_heap) #빼주고
                if min_heap: #최소힙이 남아있고, 삭제 가능하면
                    visited[min_heap[0][1]] = False #해당 key False로 바꿔주고
                    heapq.heappop(min_heap) #빼주기
            else:
                while max_heap and not visited[max_heap[0][1]]: #최대힙이 남아있고, 삭제 불가능하면
                    heapq.heappop(max_heap) #빼주고
                if max_heap: #최대힙이 남아있고, 삭제 가능하면
                    visited[max_heap[0][1]] = False #해당 key False로 바꿔주고
                    heapq.heappop(max_heap) #빼주기

    #오류 방지를 위해 마지막에 한 번더 점검
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")