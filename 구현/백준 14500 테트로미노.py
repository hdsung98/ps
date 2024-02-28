row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
total_max = 0
tetrominos = [
    [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]]
    ],
    [
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ],
    [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 0], [1, 0], [2, 0], [2, -1]],
        [[0, 0], [1, 0], [2, 0], [0, 1]],
        [[0, 0], [1, 0], [2, 0], [0, -1]],
        [[0, 0], [0, 1], [0, 2], [-1, 2]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [0, 1], [0, 2], [-1, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 0]],
    ],
    [
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 0], [1, 0], [1, -1], [2, -1]],
        [[0, 0], [0, 1], [-1, 1], [-1, 2]],
        [[0, 0], [0, 1], [1, 1], [1, 2]]
    ],
    [
        [[0, 0], [1, 0], [2, 0], [1, 1]],
        [[0, 0], [1, 0], [2, 0], [1, -1]],
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 0], [0, 1], [0, 2], [-1, 1]],
    ]
]


def calc_cur_tetro(y, x, tetro):
    tetro_max = 0
    for shape in tetro:
        score = 0
        for dy, dx in shape:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < row and 0 <= nx < col):
                break
            score += board[ny][nx]
        tetro_max = max(tetro_max, score)
    return tetro_max


for i in range(row):
    for j in range(col):
        for tetromino in tetrominos:
            total_max = max(total_max, calc_cur_tetro(i, j, tetromino))

print(total_max)

# `````````````````
import sys;

input = sys.stdin.readline  # readline에 괄호붙이지마라


def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):  # 프루닝: 지금까지 결과 + 남은블록*블록최댓값
        return
    if idx == 3:  # 네개 블록 다봤을때 (탈출조건)
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:  # 두번째 블록 뎁스에서 세번째블록 선택
                    visit[nr][nc] = 1  # 세번째 블록 선택만하고 실제로 거기서 탐색은 안함
                    dfs(r, c, idx + 1, total + arr[nr][nc])  # 두번째블록으로 복귀해 마지막 블록선택(ㅏ ㅗ ㅜ ㅓ 모양 유발)
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))  # 2차원 배열 최댓값

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
