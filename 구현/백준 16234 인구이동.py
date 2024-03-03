# "일회성 정보는 굳이 함수 밖으로 갖고 나가지말고 쓰고 갖다버려"
# = 한 연합국 내의 회원국 정보는 인구이동만 계산하고나면 쓸모 없다
# = bfs내에서 연합국 찾고 인구이동까지 업데이트 다하고, 리턴값에 연합국리스트 넣지마라.
# = 굳이 모든 연합을 다 구할 필요도 없다. 어차피 인구이동은 연합내에서 독립적으로 이뤄지므로,
# 연합국을 구하는 함수를 여러번 호출해 연합국 조합을 모두 저장하는 짓은 쓸모없었다.

import sys
from collections import deque

input = sys.stdin.readline
board_size, l_pop, m_pop = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(board_size)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def find_union(y, x, visited):
    total_pop = board[y][x]
    q = deque([(y, x)])
    union = [(y, x)]

    while q:
        cy, cx = q.popleft()
        visited[cy][cx] = True
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < board_size and 0 <= nx < board_size and not visited[ny][nx]:
                if l_pop <= abs(board[cy][cx] - board[ny][nx]) <= m_pop:
                    q.append((ny, nx))
                    union.append((ny, nx))
                    visited[ny][nx] = True
                    total_pop += board[ny][nx]  # 연합인구를 루프 다 끝나고 sum 사용하는게 아니라 "그때그때 구성요소 누적"
    for i, j in union:
        board[i][j] = total_pop // len(union)
    return len(union) > 1  # 표현 방식 숙지, 1개 발견은 연합발견 실패..


loop_cnt = 0
while True:
    visited = [[False] * board_size for _ in range(board_size)] # 매 루프때마다 연합설정 bfs는 처음부터 시작하므로
    found_union = False
    for y in range(board_size):
        for x in range(board_size):
            if not visited[y][x] and find_union(y, x, visited):
                found_union = True

    if not found_union:
        break
    loop_cnt += 1

print(loop_cnt)



# import sys
# from collections import deque
#
# input = sys.stdin.readline
# board_size, l_pop, m_pop = map(int, input().strip().split())
# board = [list(map(int, input().strip().split())) for _ in range(board_size)]
# dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#
#
# def find_union(y, x, visited):
#     q = deque([(y, x)])
#     union, found = [(y, x)], False # found 선언도 불필요...
#     tmp_visited = [[False] * board_size for _ in range(board_size)] # 불필요함 어차피 visited는 한사이클 내내 유지되는데...
#     tmp_visited[y][x] = True
#     while q:
#         cy, cx = q.popleft()
#         visited[cy][cx] = True
#         # print(cy, cx)
#         for dy, dx in dir:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < board_size and 0 <= nx < board_size and not tmp_visited[ny][nx]:
#                 if l_pop <= abs(board[cy][cx] - board[ny][nx]) < m_pop: # <= m_pop 등호 놓침
#                     q.append((ny, nx))
#                     union.append((ny, nx))
#                     found = True
#                 tmp_visited[ny][nx] = True
#     return union, found # union돌려주지마..그냥 여기서 다 연합국 인구이동 계산해..
#
#
#
# loop_cnt = 0
# while True:
#     visited = [[False] * board_size for _ in range(board_size)]
#     stay = False
#     for y in range(board_size):
#         for x in range(board_size):
#             if not visited[y][x]:
#                 union, found = find_union(y, x, visited)
#                 board[y][x] = sum(board[i][j] for i, j in union) // len(union) # 치명적 실수!!
#                 print("found union: ", union)
#                 if not stay:
#                     stay = found
#
#     if stay:
#         loop_cnt += 1
#     else:
#         break
#
# print(loop_cnt)