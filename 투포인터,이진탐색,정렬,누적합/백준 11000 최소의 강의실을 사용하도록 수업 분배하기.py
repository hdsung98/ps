import sys
import heapq

input = sys.stdin.readline  # 입력이 엄청난 경우에는 필수

schedule = [list(map(int, input().strip().split())) for _ in range(int(input().strip()))]
schedule.sort()

end_heap = []
heapq.heappush(end_heap, schedule[0][1])
room = 1
for i in range(1, len(schedule)):
    if schedule[i][0] < end_heap[0]:
        room += 1
    else:
        heapq.heappop(end_heap)

    heapq.heappush(end_heap, schedule[i][1]) # 핵심 3 !!: 최우선

print(room)

# -----------------------------------------
# 비효율적인 풀이

input = sys.stdin.readline

schedule = [list(map(int, input().split())) for _ in range(int(input()))]
heapq.heapify(schedule)  # heappop도 O(log n)이다. 한번 정렬해두고 인덱스 조회하는게 효과적. 굳이 힙으로 관리할 필요 없는 것은 하지말자

end_heap = []  # 핵심: 매 루프 "최대,최소값에 대한 조회가 필요"하며 + "그 순위가 동적으로 바뀌는" 값은 힙으로 관리하자
room = 0
while schedule:
    start, end = heapq.heappop(schedule)
    if end_heap:  # 쓸데없는 조건분기 만들지말고 처음부터 원소하나 넣고 시작하면 그만인데..
        if start < end_heap[0]:   # 핵심: 가장 빨리끝나는 수업보다 빨리시작하면 해당교실 사용불가이므로 방 증가
            room += 1
        else:
            heapq.heappop(end_heap)  # 더 이상 비교대상이 아닌 것은 pop시킴
    else:
        room += 1

    heapq.heappush(end_heap, end)

print(room)
