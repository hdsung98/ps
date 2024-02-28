# [아쉬운 풀이]
# 1. 인덱스를 0부터 시작하도록 조정해서, 초기화 및 예외처리가 빡세짐
# 2. 매 루프때마다 쓰고 버릴 시작,끝 좌표를 굳이 저장해버림

import sys

input = sys.stdin.readline

box_size, calc_num = map(int, input().strip().split())
box = [list(map(int, input().strip().split())) for _ in range(box_size)]
coord = [list(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(calc_num)]

dp = [[0] * box_size for _ in range(box_size)]
dp[0][0] = box[0][0]
for i in range(1, box_size):
    dp[i][0] = dp[i - 1][0] + box[i][0]
    dp[0][i] = dp[0][i - 1] + box[0][i]

for i in range(1, box_size):
    for j in range(1, box_size):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + box[i][j]

for x1, y1, x2, y2 in coord:
    vert_sub = dp[x2][y1 - 1] if y1 > 0 else 0
    horz_sub = dp[x1 - 1][y2] if x1 > 0 else 0
    inter_sub = dp[x1 - 1][y1 - 1] if x1 > 0 and y1 > 0 else 0
    result = dp[x2][y2] - vert_sub - horz_sub + inter_sub
    print(result)


# ``````````````````````````````````````````
# [좋은 풀이]
# 1. 그냥 dp를 box_size"+1"을 한변으로 하는 정사각형으로 선언하면, 인덱스 초기화도 간단해지고 인덱스 예외처리 싹 없어짐
# 2. 그냥 매 루프 때 좌표 입력받아 계산하고 갖다버림(따로 저장하지 않음)

import sys

input = sys.stdin.readline

box_size, calc_num = map(int, input().strip().split())
box = [list(map(int, input().strip().split())) for _ in range(box_size)]

# 누적 합 계산을 위한 DP 테이블 초기화 및 계산
dp = [[0] * (box_size + 1) for _ in range(box_size + 1)]
for i in range(1, box_size + 1):
    for j in range(1, box_size + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + box[i - 1][j - 1]

for _ in range(calc_num):
    x1, y1, x2, y2 = map(int, input().strip().split())
    # 구간 합 계산을 위한 로직 간소화
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
