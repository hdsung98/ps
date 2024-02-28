# n개 퀸을 가로 세로 대각선 방향에 겹쳐놓지 않는 경우의 수 문제

import sys

n = int(sys.stdin.readline())
col_visited = [False] * n
queens = []
cnt = 0


def attackable(y, x):
    # 한 말을 놓을때마다 일일히 모든 세로,가로,대각선을 visited 처리하는 것보다
    # 이미 놓인말들과 겹치지 않는지만 점검하는 것이 훨씬 효율적
    # 이 함수로 풀어도되고, 같은 대각선 상 점은 x+y, x-y가 상수임을 이용해도 된다
    for qy, qx in queens:
        if abs(qy - y) == abs(qx - x):
            return True
    return False


def dfs(row, queens):  # 각 행별로 퀸을 놓는 행위한번
    global cnt

    if len(queens) == n:  # 항상 탈출조건 먼저 고려
        cnt += 1  # 한 경우의수가 완성 됐을때 비로소 +1
        return

    for col in range(n):
        if col_visited[col]:  # 이미 퀸이 놓인 행 넘김
            continue
        if not attackable(row, col):
            queens.append((row, col))
            col_visited[col] = True
            dfs(row + 1, queens)  # 현재 row에 퀸을 특정 행에 놓은 정보를 바탕으로 다음 행 놓으러 출발
            queens.pop()  # 백트래킹
            col_visited[col] = False


dfs(0, queens)
print(cnt)
