from collections import deque

row, col, box = map(int, input().split())
total = [[0] * col for _ in range(row)]
boxes = []
# for _ in range(box):
#     lx, ly, rx, ry = map(int, input().split())
#     ly, ry = row - ly, row - ry
#     info = (lx, ly, rx, ry)
#     boxes.append(info)
#
# for lx, ly, rx, ry in boxes:
#     for i in range(ry, ly):
#         for j in range(lx, rx):
#             total[i][j] = 1

# 위처럼 굳이 루프 두번 돌지말고, ly,ry 구한 즉시 한큐에 해결가능
for _ in range(box):
    lx, ly, rx, ry = map(int, input().split())
    ly, ry = row - ly, row - ry # 세로의 상하가 뒤집혀있으므로 변환 / "칸"이 아니라 "꼭지점"이라는 점 주의
    for i in range(ry, ly):
        for j in range(lx, rx):
            total[i][j] = 1


visited = [[False] * col for _ in range(row)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(y, x):
    visited[y][x] = True
    q = deque([(y, x)])
    area = 1 # 한칸이라도 일단 존재하는 거니까 1로 초기화
    while q:
        cy, cx = q.popleft()
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
                if total[ny][nx] != 1:
                    visited[ny][nx] = True # 항상 "방문 + 큐 추가"는 필수
                    q.append((ny, nx))
                    area += 1

    return area


areas = []
for i in range(row):
    for j in range(col):
        if total[i][j] == 0 and not visited[i][j]:
            areas.append(bfs(i, j))

areas.sort() # 리턴타입 None이다
print(len(areas)) # 굳이 cnt로 집계하지말고 len으로 깔끔처리
print(' '.join(map(str, areas)))
