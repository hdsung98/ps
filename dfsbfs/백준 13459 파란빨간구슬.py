from collections import deque

row, col = map(int, input().split())
board = [[0] * col for _ in range(row)]
r, b, h = [0, 0], [0, 0], [0, 0]
for i in range(row):
    tmp = list(input())
    for j in range(col):
        board[i][j] = tmp[j]
        if board[i][j] == 'R':
            r = [i, j]
        elif board[i][j] == 'B':
            b = [i, j]
        elif board[i][j] == 'O':
            h = [i, j]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * col for _ in range(row)]
cnt = 0
q = deque([(r, b, cnt)])
while q:
    r, b, cnt = q.popleft()
    for op,mv in enumerate(dir):
        nr, nb = r, b

        if op ==1:
            pass
        while board[nr[0]][nr[1]] == '.' and not visited[nr[0]][nr[1]]:
            nr += mv
            visited[nr[0]][nr[1]] = True
        if board[nr[0]][nr[1]] == 'O':
            print(1)
            exit()
        nr -= mv
        board[nr[0]][nr[1]], board[r[0]][r[1]] = 'R', '.'

        while board[nb[0]][nb[1]] == '.':
            nb += mv
        if board[nb[0]][nb[1]] == 'O':
            print(0)
            exit()
        nb -= mv
        board[nb[0]][nb[1]], board[b[0]][b[1]] = 'B', '.'


# ````````````````````````````````
from collections import deque

row, col = map(int, input().split())
board = [[0] * col for _ in range(row)]
for i in range(row):
    tmp = list(input())  # 시작좌표를 알아야하는 경우 사용하는 방법
    for j in range(col):
        board[i][j] = tmp[j]
        if board[i][j] == 'R':
            r = (i, j)
        elif board[i][j] == 'B':
            b = (i, j)
        elif board[i][j] == 'O':
            h = (i, j)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move(ball, dy, dx):  # 파란공이건 빨간공이건 똑같이 적용되는 로직이므로 함수화
    y, x = ball[0], ball[1]
    cnt = 0
    # while문의 조건의 본질은 "언제 멈추고 싶은지"를 적는 것
    # 멈추고 싶은 때: "벽에 도달하기 직전" 또는 "구멍에 빠질때"
    # "직전"을 구현하는 법: y+dy, x+dx등 "미래형"으로 표시해, 현재 y,x값이 실제 벽에 닿지는 않게함
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt


visited = set()
q = deque([(r, b, 0)])
while q:
    r, b, cnt = q.popleft()
    # 이동횟수 10 이내, r이 구멍에 도달한 경우 종료(이걸 어떻게 표현할지를 아래 for문보다 먼저 생각하자)
    # 단일 조건으로 끝낼 수 있으면 단일조건으로 끝내자(10회일 때 and R이 구멍에 안갔을때..이런식으로 하지말고 => 10회 넘기면 R이 도달했건말건 무조건 아웃)
    if cnt > 10:
        print(0)
        exit()
    # 더 큰 조건으로 먼저 EXIT. 그리고 남은 종료조건도 단일조건으로 진술    
    if r == h:
        print(1)
        exit()

    for dy, dx in dir:
        ry, rx, r_cnt = move(r, dy, dx)
        by, bx, b_cnt = move(b, dy, dx)

        nr, nb = (ry, rx), (by, bx)
        if nb == h:  # 중요 아이디어: 빨간공이 도달했는지 여부는 안중요(도달했더라도 동시에 빠진셈이므로 어차피 거를 대상)
            continue
        if nr == nb:  # 중요 아이디어 ! : 공을 따로따로 움직이는게 아니라 한번에 움직여놓고 이동거리에 따라 "추후보정"
            if r_cnt > b_cnt:
                nr = (ry - dy, rx - dx)
            else:
                nb = (by - dy, bx - dx)

        if (nr, nb) not in visited:  # 중요 아이디어: visited는 두 공의 위치 "조합"으로 관리
            visited.add((nr, nb))
            q.append((nr, nb, cnt + 1))

print(0)

