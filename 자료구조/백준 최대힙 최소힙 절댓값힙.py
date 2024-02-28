# [heapq 자료구조의 heappush, heappop을 활용]

import sys, heapq

input = sys.stdin.readline

pq = []
calc_num = int(input().strip())
for _ in range(calc_num):
    calc = int(input().strip())
    if calc == 0:
        if len(pq):
            print(heapq.heappop(pq))  # heappop(배열) = 자동으로 heapify
        else:
            print(0)
    else:
        heapq.heappush(pq, calc)  # heappush(배열,값) = 자동으로 heapify

# `````````````````
# [maxheap 구현]
import sys, heapq

input = sys.stdin.readline

pq = []
calc_num = int(input().strip())
for _ in range(calc_num):
    calc = int(input().strip())
    if calc == 0:
        if len(pq):
            print(-heapq.heappop(pq))  # 출력할때만 복원
        else:
            print(0)
    else:
        heapq.heappush(pq, -calc)  # 저장할때 부호만 바꿔서(가장 큰수가 가장 작은수가 됨)

# `````````````````
# [절댓값 max heap 구현]
import sys, heapq

input = sys.stdin.readline

pq = []
calc_num = int(input().strip())
for _ in range(calc_num):
    calc = int(input().strip())
    if calc == 0:
        if pq:
            val, sign = heapq.heappop(pq)  # 사전식 저장됐으므로 같은 절댓값인 경우 음수가 root
            print(val * sign)  # 부호 복원
        else:
            print(0)
    else:
        heapq.heappush(pq, (abs(calc), 1 if calc > 0 else -1))  # 부호정보 추가로 저장(원소가 튜플인경우 사전식으로 저장됨)
