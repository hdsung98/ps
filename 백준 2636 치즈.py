from collections import deque

row, col = map(int, input().split())
board = [[0] * col for _ in range(row)]
cheese_cnt, melted_acc, cycle_cnt = 0, 0, 0
for i in range(row):
    tmp = list(map(int, input().split()))
    for j in range(col):
        board[i][j] = tmp[j]
        if tmp[j] == 1:
            cheese_cnt += 1

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def find_melt():
    q = deque([(0, 0)])
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True
    found = []
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < row and 0 <= nx < col and not visited[ny][nx]):
                continue
            if board[y][x] == 0:
                if board[ny][nx] == 1 and not (y, x) in found:
                    found.append((ny, nx))
                q.append((ny, nx))
                visited[ny][nx] = True

    return found


while cheese_cnt > melted_acc:
    found = find_melt()
    if found:
        for y, x in found:
            board[y][x] = 0
    last_melted = len(found)
    melted_acc += last_melted
    cycle_cnt += 1

print(cycle_cnt)
print(last_melted)
