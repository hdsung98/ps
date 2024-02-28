# 꽝: 이동,자리유지 = 합,s,b 변화 없음 / 사라지면 = 똑같거나 증가
# 볼: 이동= 변화없거나 s1증가,b1감소 / 자리유지 = 변화없음 / 사라지면 =
# 스트: 이동= s1 감소, b1증가

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [[1, 0], [1, 1], [1, -1], [1, 2], [1, -2]]
q = deque([(-1, 1, 0)])

min_curve = float('inf')
# final = [] <= 비효율적이다
while q:
    y, x, cnt = q.popleft()
    if y == n - 1:
        min_curve = min(min_curve, cnt)
        continue
        # final.append(cnt)
    # cur_row_min = float('inf')
    for dy, dx in dirs:
        ny, nx, n_cnt = y + dy, x + dx, cnt  # n_cnt 루프 돌기전에 초기화해라
        if (0 <= nx < 3) and (0 <= ny < n) and (graph[ny][nx] != 1):
            if dx != 0:
                n_cnt += 1  # 초기화해놓고 1 더하기
            # if cur_row_min > n_cnt: <=굳이 추가과정에서 최소집계를 할 필요 없음
            #     cur_row_min = n_cnt
            q.append((ny, nx, n_cnt))
    # min_curve = cur_row_min
print(min_curve)
# print(min(final))

