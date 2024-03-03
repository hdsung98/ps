# 문제
# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
# 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
#
# 입력
# 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
#
# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
#
# 따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.
#
# 출력
# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
#
# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.
#
# 예제 입력 1
# 4 4
# 3 0 1 4
# 예제 출력 1
# 5

# 핵심: 물이 고이는 것은 직전직후 셀에 의해 영향을 받는게 아니라 한참 멀리있는 벽에 의해서다
# 셀단위로 처리하지말고(bfs,백트래킹 등..) , col단위로 처리해야한다

import sys

input = sys.stdin.readline

row, col = map(int, input().strip().split())
blocks = list(map(int, input().strip().split()))

cnt = 0
for i in range(1, col - 1):
    l_max, r_max = max(blocks[:i]), max(blocks[i + 1:])
    if not (l_max > blocks[i] and r_max > blocks[i]):
        continue
    limit = min(l_max, r_max)
    cnt += (limit - blocks[i])

print(cnt)

