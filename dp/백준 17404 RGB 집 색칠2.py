# import sys
#
# input = sys.stdin.readline
#
# house_num = int(input().strip())
# costs = []
# for _ in range(house_num):
#     costs.append(list(map(int, input().split())))
#
# dp = [[[float('inf')] * 3 for _ in range(3)] for _ in range(house_num)]
#
# dp[0][0][0], dp[0][1][1], dp[0][2][2] = costs[0][0], costs[0][1], costs[0][2]
#
# for depth in range(1, house_num):
#     for first in range(3):
#         if depth == 1:
#             for left_color in list({0, 1, 2} - {first}):
#                 try:
#                     dp[1][left_color][first] = dp[0][first][first] + costs[1][left_color]
#                 except:
#                     print("error: ", left_color, first)
#
#         elif depth == house_num - 1:
#             for right_before in range(3):
#                 final = list({0, 1, 2} - {first, right_before})
#
#                 dp[depth][final[0]][first] = \
#                     dp[depth - 1][right_before][first] + costs[depth][final[0]]
#                 if len(final) == 2:
#                     dp[depth][final[1]][first] = \
#                         dp[depth - 1][right_before][first] + costs[depth][final[1]]
#
#         else:
#             dp[depth][0][first] = \
#                 min(dp[depth - 1][1][first], dp[depth - 1][2][first]) + costs[depth][0]
#             dp[depth][1][first] = \
#                 min(dp[depth - 1][0][first], dp[depth - 1][2][first]) + costs[depth][1]
#             dp[depth][2][first] = \
#                 min(dp[depth - 1][0][first], dp[depth - 1][1][first]) + costs[depth][2]
#
# result = float('inf')
# for first in range(3):
#     for final in list({0, 1, 2} - {first}):
#         result = min(result, dp[house_num-1][final][first])
#
# print(result)

import sys

input = sys.stdin.readline
house_num = int(input().strip())
costs = []
for _ in range(house_num):
    costs.append(list(map(int, input().strip().split())))

# dp 설계 : [현재 집][현재 집 색][첫번째 집 색]
# 첫번째 집의 색 + 직전 집의 색 정보를 보존해야 마지막 색 선택시 최적의 답을 정할 수 있으므로 3차원!
dp = [[[float('inf')] * 3 for _ in range(3)] for _ in range(house_num)]
for i in range(3):
    dp[0][i][i] = costs[0][i]

for depth in range(1, house_num):
    for cur in range(3):
        for first in range(3):
            if depth == 1 and first != cur:  # 굳이 list(set(전체색)-set(현재색))할 필요 없이 단순 조건문으로 구현하는 것이 효율적
                dp[depth][cur][first] = dp[depth - 1][first][first] + costs[depth][cur]
            else:
                for prev in range(3):
                    if (depth < house_num - 1 and prev != cur) or (
                            depth == house_num - 1 and prev != cur and first != cur):
                        # "본인"을 min에 넣고 "루프" 돌리면, 굳이 min 내에 모든 원소를 일일히 기입하지않아도 됨.
                        dp[depth][cur][first] = min(dp[depth][cur][first],
                                                    dp[depth - 1][prev][first] + costs[depth][cur])

result = float('inf')
for final in range(3):
    result = min(result, min(dp[house_num - 1][final]))

print(result)
