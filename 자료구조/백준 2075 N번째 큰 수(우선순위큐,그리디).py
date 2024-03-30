# 시간복잡도는 다 때려박은 뒤 N번 POP하는 것이나, 이 방법이나 N제곱logN이지만
# 공간복잡도가 큐 사이즈를 N으로 고정하는 측면에서 이 방법이 훨씬 효과적

# 유선순위 큐는 어떤 탐색 범위에서 top N개를 follow up 하고 싶을 때 사용

import sys, heapq

input = sys.stdin.readline

line_size = int(input())
heap = list(map(int, input().split()))  # 한번에 모든 원소 다 때려 박으면 메모리 초과
heapq.heapify(heap)
for _ in range(1, line_size):
    for e in map(int, input().split()):  # 새로운 N개의 입력
        if e > heap[0]:  # 각 사이클 마다 최소 원소 N개 솎아냄
            heapq.heappushpop(heap, e)  # push,pop 따로 따로 보다 효과적

print(heap[0])
