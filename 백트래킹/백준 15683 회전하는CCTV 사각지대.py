row, col = map(int, input().split())
room = []
cctvs = []
open_space = 0
for i in range(row):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    for j, val in enumerate(tmp):
        if val == 0:
            open_space += 1
        elif 1 <= val <= 5:
            cctvs.append((i, j, val))

dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
type_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}

min_black = float('inf')
visited = [[False] * col for _ in range(row)]


def search(direction_set, y, x):
    global visited
    cnt = 0

    for dir_num in direction_set:
        ny, nx = y, x
        dy, dx = dir[dir_num]
        while 0 <= ny < row and 0 <= nx < col and not visited[ny][nx] and room[ny][nx] != 6:
            if room[ny][nx] == 0:
                visited[ny][nx] = True
                cnt += 1
            ny, nx = ny + dy, nx + dx
    return cnt


def dfs(depth, total_searched):
    global min_black, visited
    if depth == len(cctvs):
        min_black = min(min_black, open_space - total_searched)
        # visited = [[False] * col for _ in range(row)] 절대 바텀케이스에서 원큐에 초기화 금지!! 루트로 돌아가는게 아니다!
        return

    y, x, type = cctvs[depth]
    for direction_set in type_dir[type]:
        visited_backup = [row[:] for row in visited]
        searched = search(direction_set, y, x)
        # total_searched += searched dfs for 문에서 절대 누적을 하지마라!!!!!
        dfs(depth + 1, total_searched+searched)
        # visited = visited_backup 비효율적이다. 재귀 바닥찍고 한 뎁스 올라올때마다 이미 복원된 애를 계속 복원시키는 헛짓거리


dfs(0, 0)
print(min_black)
