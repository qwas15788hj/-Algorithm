import heapq


def solution(book_time):
    answer = 0
    arr = []

    for i in range(len(book_time)):
        a = [0] * 2
        a[0] = (int(book_time[i][0][0]) * 10 + int(book_time[i][0][1])) * 60 + int(book_time[i][0][3]) * 10 + int(
            book_time[i][0][4])
        a[1] = (int(book_time[i][1][0]) * 10 + int(book_time[i][1][1])) * 60 + int(book_time[i][1][3]) * 10 + int(
            book_time[i][1][4])
        arr.append(a)

    arr.sort(key=lambda x: x[0])

    heap = []
    heapq.heappush(heap, arr[0][1])  # 퇴실시간 넣기

    for i in range(1, len(arr)):
        if arr[i][0] - 10 >= heap[0]:  # 입실시간+10 >= 퇴실시간이면 해당 방 사용 가능
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i][1])
        else:
            heapq.heappush(heap, arr[i][1])
        # print(heap)
    return len(heap)