# 문제
# 뿌요뿌요의 룰은 다음과 같다.
#
# 필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.
#
# 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.
#
# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
#
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.
#
# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.
#
# 입력
# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
#
# 이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
#
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
#
# 입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.
#
# 출력
# 현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
#
# 예제 입력 1
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# .Y....
# .YG...
# RRYG..
# RRYGG.
# 예제 출력 1
# 3

from collections import deque

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
field = [list(input()) for _ in range(12)]


def check_pop(y, x, visited):
    cur_color = field[y][x]
    visited[y][x] = True

    q = deque([(y, x)])
    cells = [(y, x)]
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx]:
                if field[ny][nx] == cur_color:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cells.append((ny, nx))

    return cells


# 순회 범위가 얼마 안될땐 그냥 다 돌자
def find_all_pops():
    visited = [[False] * 6 for _ in range(12)]

    pop = False
    for i in range(12):  # 어차피 다해봤자 72개 셀이기 때문에 굳이 bfs로 검사안한 애 찾지말고 다 순회하는게 놓치는거 없음
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                cells = check_pop(i, j, visited)
                if len(cells) >= 4:  # 찾은 셀 길이로 판단하면 되므로 굳이 pop 성공여부 boolean값 따로 받을 필요 없음
                    pop = True
                    for y, x in cells:
                        field[y][x] = '.'

    return pop


# 구현은 특수 일부 케이스에 착안해 코드를 짜지말자
# 오히려 단순 무식하게 짜는게 예외없고 코드도 간략
# 블록 떨어짐의 본질은 현재 블록이 어느 높이에 떠있건, "바닥부터 순서대로 공백없이 쌓는것"
def drop():
    for c in range(6):  # 각 행에 대해서
        to_drop = []
        for r in range(11, -1, -1):  # 해당 행의 바닥부터 꼭대기로 거슬러 올라가며 떨어뜨릴 모든 문자 수집(역방향 순서인 것이 중요!!!)
            if field[r][c] != '.':
                # 사실상 빈칸이 아닌 블럭이 있는 모든 셀 검사, 바닥에 붙어 있는 블록들까지 포함
                # 공중에 떠있는 덩어리가 1개라는 보장 없음
                to_drop.append(r)

        for i, r in enumerate(to_drop):
            field[11 - i][c] = field[r][c]  # 기존에 얼만큼 공중에 떠있었나 그 높이는 중요하지 않음!!!!! 순서만 지켜서 바닥에서부터 쌓으면 그만
        for r in range(12 - len(to_drop)):  # 바닥부터 쌓인 블록 길이 제외하고 나머지 상단 다 빈칸 처리!!!!
            # for r in to_drop 으로 하면 안됨
            # 처음 블록 수집 했던 위치가 지금 빈칸이라는 보장 없음(떨어짐 처리한 후 그 셀에 현재는 다른 블록이 있을 수 있다)
            field[r][c] = '.'


streak_cnt = 0
while True:
    if find_all_pops():
        drop()
        streak_cnt += 1
    else:
        break
print(streak_cnt)

# for j in range(6):
#     bottom = 11
#     while bottom >= 0:
#         if field[bottom][j] == '.':
#             break
#         bottom -= 1
#
#     if bottom == 0:
#         continue
#
#     top, drop = bottom, False
#     while top > 0:
#         if field[top - 1][j] != '.':
#             drop = True
#             break
#         top -= 1
#
#     if drop:
#         len = bottom - top + 1
#         for i in range(bottom, top - 1, -1):
#             field[i][j] = field[i - len][j]
#             field[i - len][j] = '.'


# def find_start():
#     for j in range(6):
#         if field[11][j] != '.':
#             return j
#     return None

# def find_all_pops(col):
#     visited = [[False] * 6 for _ in range(12)]
#
#     q = deque([(11, col)])
#     pop = False
#     while q:
#         y, x = q.popleft()
#         for dy, dx in dir:
#             ny, nx = y + dy, x + dx
#             if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx]:
#                 if field[ny][nx] != '.':
#                     cells = check_pop(ny, nx, visited)
#                     if len(cells) >= 4:
#                         pop = True
#                         for y, x in cells:
#                             field[y][x] = '.'
#
#                     if cells:
#                         q.append(cells[-1])
#
#     return pop
