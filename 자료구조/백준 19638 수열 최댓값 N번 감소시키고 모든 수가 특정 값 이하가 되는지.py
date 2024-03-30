import sys,heapq

input = sys.stdin.readline

population, threshold, hammer_limit = map(int, input().split())
giants = [-int(input()) for _ in range(population)]  # 음수로 넣어서 최대힙 구성

heapq.heapify(giants)  # 최댓값을 추적해야하며, 그 순위가 동적으로 변하므로 우선순위큐가 적절!
cnt = 0
for _ in range(hammer_limit):
    if -giants[0] < threshold or -giants[0] <= 1:  # 엣지 케이스: 최댓값이 1이라 더 나누는 의미가 없는 것
        break
    max_giant = -heapq.heappop(giants)
    cnt += 1
    heapq.heappush(giants, -(max_giant // 2))

if -giants[0] < threshold:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-giants[0])
