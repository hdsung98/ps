# import sys
#
# input = sys.stdin.readline
#
# row, col = map(int, input().strip().split())
# board = [list(input().strip()) for _ in range(row)]
#
# max_cnt = 0
# dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# history = set()
#
#
# def dfs(y, x, cnt):
#     global max_cnt
#
#     max_cnt = max(max_cnt, cnt)
#     if max_cnt == 26:  # 최대 길이 도달
#         return
#
#     for dy, dx in dir:
#         ny, nx = y + dy, x + dx
#         if 0 <= ny < row and 0 <= nx < col and board[ny][nx] not in history:
#             history.add(board[ny][nx])
#             dfs(ny, nx, cnt + 1)
#             history.remove(board[ny][nx])
#
#
# history.add(board[0][0])
# dfs(0, 0, 1)
# print(max_cnt)


# set이 아무리 탐색에 O(1)이라지만 상수값이 상당히 크며,
# 해시충돌날 경우 WORST CASE에 O(n)일수도 있다.
# 차라리, visited 범위가 확정적이고 선형적인 경우, 전역 visited로 관리하는 것이 시간상 유리


row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]
max_cnt = 0
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [False] * 26


def char_to_index(c):
    return ord(c) - ord('A')


def dfs(y, x, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if max_cnt == 26:
        return

    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < row and 0 <= nx < col:
            next_char_index = char_to_index(board[ny][nx])
            if not visited[next_char_index]:
                visited[next_char_index] = True
                dfs(ny, nx, cnt + 1)
                visited[next_char_index] = False


visited[char_to_index(board[0][0])] = True
dfs(0, 0, 1)
print(max_cnt)
