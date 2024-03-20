# 문제
# N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다.
# 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다.
# 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다.
#
#
# 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다.
# 그러므로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다.
# 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.

#
# 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다.
# 그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다.
# 또한, 각 0과 1은 하나의 공백으로 분리되어 있다.
#
# 출력
# 출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.
#
# 예제 입력 1
# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 예제 출력 1
# 4

import sys
from collections import deque

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def check_outer_air():
    visited = [[False] * col for _ in range(row)]
    q = deque([(0, 0)])  # 테두리는 치즈가 안놓인다는 보장이 있으므로 안전한 bfs 시작점
    if field[0][0] == 0: field[0][0] = -1

    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
                if field[ny][nx] <= 0: # 외부공기거나, 치즈내부 공기(이제 외부와 연결될 공기)거나. 하여튼 치즈본체가 아닌 부분만 탐색
                    field[ny][nx] = -1  # 치즈 내 공간과 분리 표현
                    q.append((ny, nx))
                    visited[ny][nx] = True


def find_melting_spot():
    check_outer_air()

    found = []
    for y in range(row):
        for x in range(col):
            if field[y][x] == 1:
                air = 0
                for dy, dx in dir:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < row and 0 <= nx < col:
                        if field[ny][nx] == -1: # 외부 공기인 경우!(치즈 내부 공기는 고려대상x)
                            air += 1
                if air >= 2:
                    found.append((y, x))
    return found


def melt(found):
    for y, x in found:
        field[y][x] = -1


input = sys.stdin.readline
row, col = map(int, input().strip().split())
field = [list(map(int, input().strip().split())) for _ in range(row)]

loop_cnt = 0
while True:
    found = find_melting_spot()
    if len(found) > 0:
        melt(found)
        loop_cnt += 1
    else:
        break

print(loop_cnt)
