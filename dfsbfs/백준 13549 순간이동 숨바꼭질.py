from collections import deque

total_len = 100001 # 인덱스 끝값 항상 고려하자

start, end = map(int, input().split())
if start==end: # 엣지 케이스
    print(0)
    exit()

q = deque([(start, 0)])
visited = [False] * total_len
visited[start] = True # 시작점 방문 항상 초기화할것
while q:
    pos, cnt = q.popleft()

    if pos == end:
        print(cnt)
        exit()

    for i, next in enumerate([pos * 2, pos - 1, pos + 1]): # 순간이동은 비용이 0이므로 우선 탐색!!
        if 0 <= next < total_len and not visited[next]:
            visited[next] = True
            q.append((next, cnt + 1 if i != 0 else cnt))


