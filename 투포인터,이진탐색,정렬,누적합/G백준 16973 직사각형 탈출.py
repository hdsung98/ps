# 문제
# N×M 격자판에 H×W 크기 직사각형을 (Sr, Sc)에서 (Fr, Fc)로 이동시키는 최소 이동 횟수를 구하라.
# 격자판에는 빈 칸과 벽이 있으며, 직사각형은 벽이 있는 칸이나 격자판 바깥으로 이동할 수 없다.
# 직사각형은 한 번에 상하좌우 한 칸 이동 가능.

# 입력
# 첫째 줄에 격자판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 각 칸의 정보가 주어진다. 0은 빈 칸, 1은 벽이다.
# 마지막 줄에는 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc가 주어진다.
# 격자판의 좌표는 (r, c) 형태이고, r은 행, c는 열이다. 1 ≤ r ≤ N, 1 ≤ c ≤ M을 만족한다.

# 출력
# 첫째 줄에 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

# 제한
# 2 ≤ N, M ≤ 1,000
# 1 ≤ H ≤ N
# 1 ≤ W ≤ M
# 1 ≤ Sr ≤ N-H+1
# 1 ≤ Sc ≤ M-W+1
# 1 ≤ Fr ≤ N-H+1
# 1 ≤ Fc ≤ M-W+1
# 입력으로 주어진 직사각형은 격자판을 벗어나지 않고, 직사각형이 놓여 있는 칸에는 벽이 없다.

# 예제 입력 1
# 4 5
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 2 2 1 1 1 4
# 예제 출력 1
# 7


# BFS 사용 근거: 2차원 배열 내 한지점에서 다른 지점으로의 최소 이동횟수이므로
# 발상의 전환: 장애물 존재여부 검사에 "누적합" 사용
    # [BAD] 매 이동때마다 사각형 안에 벽이 존재하는지 계산 (사각형 내 모든 셀에 대해, 벽 좌표 리스트를 일일이 순회)
    # [GOOD] 누적합!: 구간 내 존재하는 장애물의 개수를 누적합으로 미리 계산해둠

import sys
from collections import deque

input = sys.stdin.readline
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def is_safe(y, x):
    ey, ex = y + height, x + width
    obstacle = acc_sum[ey][ex] - acc_sum[ey][x] - acc_sum[y][ex] + acc_sum[y][x]

    return obstacle == 0


row, col = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(row)]
height, width, sy, sx, fy, fx = map(int, input().split())

acc_sum = [[0] * (col + 1) for _ in range(row + 1)]
for i in range(1, row + 1):
    for j in range(1, col + 1):
        acc_sum[i][j] = acc_sum[i - 1][j] + acc_sum[i][j - 1] - acc_sum[i - 1][j - 1] + field[i - 1][j - 1]

q = deque([(sy - 1, sx - 1, 0)])
visited = [[False] * col for _ in range(row)]
visited[sy - 1][sx - 1] = True

while q:
    y, x, cnt = q.popleft()
    if (y, x) == (fy - 1, fx - 1):
        print(cnt)
        exit()

    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny <= row - height and 0 <= nx <= col - width and not visited[ny][nx]:
            visited[ny][nx] = True
            if is_safe(ny, nx):
                q.append((ny, nx, cnt + 1))

print(-1)
