# [시간초과 풀이:DFS]
#
# 한번 끝 뎁스까지 쭉 계산하고 난 다음, 완전 초기화 후 다음 경우의수 계산하므로
# 중간계산 결과가 보존되지않고 다 날아가버리는 단점있음
# O(3^house_num)

import sys

input = sys.stdin.readline

house_num = int(input().strip())
paint_price = [list(map(int, input().strip().split())) for _ in range(house_num)]
min_price = float('inf')


def dfs(cur, prev_color, total_price):
    global min_price
    if cur == house_num:
        min_price = min(min_price, total_price)
        return

    for color in range(3):
        if color != prev_color:
            total_price += paint_price[cur][color]
            dfs(cur + 1, color, total_price)
            total_price -= paint_price[cur][color]


dfs(0, -1, 0)
print(min_price)
# ````````````````````````````````````````````
#
# [효율적 풀이: DP]
# 각 뎁스+색상 별 최소 값을 계속 보존해 다음 뎁스에 활용하기 때문에 효율적
# O(house_num)

import sys

input = sys.stdin.readline
house_num = int(input().strip())
paint_price = [list(map(int, input().strip().split())) for _ in range(house_num)]
dp = [[0] * 3 for _ in range(house_num)]
dp[0] = paint_price[0]

for i in range(1, house_num):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + paint_price[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + paint_price[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + paint_price[i][2]

print(min(dp[house_num - 1]))
