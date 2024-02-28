row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * col for _ in range(row)]
cnt = 0


def dfs(y, x):  # 최단거리가 아니고 최단경로의 "갯수"를 구하므로 한번 갈때 끝까지 찍어버리는 dfs가 적절
    global cnt  # cnt는 모든 재귀 콜에서 누적돼야하므로 global 처리
    visited[y][x] = True
    if y == row - 1 and x == col - 1:
        cnt += 1
        return
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
            if graph[y][x] > graph[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)
                visited[ny][nx] = False  # 한 경로 탐색이 끝나고 다른 방향탐색을 할때 영향을 주지않기 위해
                반드시
                visited
                False
                복구
                필요


dfs(0, 0)
print(cnt)

# ``````````````````````````````
# 그러나 잘생각해보면
# 한 셀에서 종점까지 가능한 경로갯수는 맵이 바뀌지않는 한 고정적이다.
# 위 풀이는, 이전 탐색때 지나갔던 셀이어도 이번 탐색 때 처음방문하는 것이면 종점까지 거리를 또 계산한다.
# 만약 각 셀 별로 해당 셀에서 종점까지의 가능경로를 저장해둔다면,
# 다음에 어떤 경로를 통해서 해당 셀에 도착하던지간에, 이 셀부터 종점까지의 경로갯수는 알기떄문에
# 더 탐색을 진행하는 불필요한 계산을 생략하게 되는 것이다.

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * col for _ in range(row)]


def dfs(y, x, memo):
    if y == row - 1 and x == col - 1:
        return 1
    if memo[y][x] != -1:
        return memo[y][x]  # 이미 목적지까지 경로 개수 계산된 셀이면 더이상 탐색하지마라

    memo[y][x] = 0  # 현재 셀에대한 계산 시작(누적을 위해 0으로 세팅,-1은 계산 안됐을때 플래그)
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < row and 0 <= nx < col and graph[ny][nx] < graph[y][x]:
            memo[y][x] += dfs(ny, nx, memo)  # 현재 셀에서 목적지까지 경로 갯수 누적
    return memo[y][x]


memo = [[-1] * col for _ in range(row)]
print(dfs(0, 0, memo))
