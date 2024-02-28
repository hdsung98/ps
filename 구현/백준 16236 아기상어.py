import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
aquarium = [[0] * N for _ in range(N)]
shark_pos, shark_size, ate = (0, 0), 2, 0
for i in range(N):
    tmp = list(map(int, input().strip().split()))
    for j in range(N):
        cur = tmp[j]
        if cur:
            if cur == 9:
                shark_pos = (i, j)
            else:
                aquarium[i][j] = cur

dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def bfs():  # 현재위치에서 최단거리로 이동하고 먹고 레벨업
    global shark_pos, shark_size, ate

    cy, cx = shark_pos
    q = deque([(cy, cx, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[cy][cx] = True
    while q:
        y, x, cnt = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if aquarium[ny][nx] <= shark_size:
                    visited[ny][nx] = True
                    if 0 < aquarium[ny][nx] < shark_size:
                        aquarium[ny][nx] = 0
                        ate += 1
                        if ate == shark_size:
                            shark_size += 1
                            ate = 0
                        shark_pos = (ny, nx)
                        return True, cnt + 1
                    q.append((ny, nx, cnt + 1))

    return False, cnt


success = True
total_move = 0
while success:
    success, moved = bfs()
    if success:
        total_move += moved
    print("cur move:", moved, "total moved:", total_move)
print(total_move)


# ````````````````````````````````
#
# 위 문제 풀이의 문제점
# 0. 정렬안함
# 1. bfs내에서 조건충족시(먹을 수 있는 물고기 만나면) 바로 동적으로 상태변화시킴(거리,높이,좌우 정렬기준있음에도 불구)
# 2. bfs 한 사이클의 역할을 분명히 정하지못함(현재위치,현재사이즈 두가지 제약을 걸고 한 bfs당 한마리만 잡아야되는데, 사이즈를 bfs내에서 동적으로 키워버림)


from collections import deque

N = int(input())
aquarium = [list(map(int, input().split())) for _ in range(N)]

# 상어 초기 위치 및 크기 설정
shark_size = 2
shark_pos = None

for i in range(N):
    for j in range(N):
        if aquarium[i][j] == 9:
            shark_pos = (i, j)
            aquarium[i][j] = 0  # 상어의 시작 위치를 빈 칸으로 설정

# 이동 방향 - 상, 좌, 우, 하 (문제의 조건에 맞게 우선순위 설정)
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(shark_pos, shark_size):
    q = deque([(shark_pos, 0)])  # (위치, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = True
    fishes = []  # 먹을 수 있는 물고기 리스트

    while q:
        (y, x), dist = q.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if aquarium[ny][nx] <= shark_size:  # 이동 가능 조건
                    visited[ny][nx] = True
                    q.append(((ny, nx), dist + 1))

                    if 0 < aquarium[ny][nx] < shark_size:  # 먹을 수 있는 물고기
                        fishes.append(((ny, nx), dist + 1))

    # 먹을 수 있는 물고기 중 조건에 맞는 물고기 선택
    if fishes:
        fishes.sort(key=lambda x: (x[1], x[0][0], x[0][1]))  # 거리, y좌표, x좌표 순으로 정렬
        return fishes[0]  # 가장 우선순위가 높은 물고기 반환
    return None


time = 0
ate = 0

while True:
    result = bfs(shark_pos, shark_size)
    if result is None:  # 더 이상 먹을 물고기가 없음
        break
    else:
        next_pos, dist = result
        aquarium[next_pos[0]][next_pos[1]] = 0  # 물고기 먹기
        shark_pos = next_pos  # 상어 위치 업데이트
        time += dist  # 시간(거리) 추가
        ate += 1
        if ate == shark_size:  # 상어 크기만큼 물고기를 먹었다면 크기 증가
            shark_size += 1
            ate = 0
        print("ate fish at:", next_pos[0], next_pos[1], "size now:", shark_size, "ate by far:", ate)
        print("cur move:", dist, "total moved:", time)
print(time)
