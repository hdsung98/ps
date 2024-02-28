from collections import deque

total, start, dest, up, down = map(int, input().split())
q = deque([(start, 0)])
dir = [up, -down]
visited = [False] * (total + 1)
if start == dest:  # 엣지 케이스 누락
    print(0)
    exit()

while q:
    cur, cnt = q.popleft()
    for mv in dir:
        next = cur + mv
        if next == dest:
            print(cnt + 1)
            exit()
        if 1 <= next <= total and not visited[next] and mv != 0:
            visited[next] = True
            # cnt +=1 <= 이렇게 누적해버리면 for문 안에서는 값이 +1이 아니라 +2누적될수도 있다
            q.append((next, cnt + 1))  # 반드시 큐에 추가할때만 누적없이 1 increment시킬 것
print("use the stairs")
