n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[float("inf")] * 3 for _ in range(n)]
idx = [0, 1, 2]
if graph[0][1] == 1:
    dp[0][0] = dp[0][2] = 1

for i in range(1, n):
    for j in range(3):
        if graph[i][j] == 0:
            if j == 0:
                cur_min = min(dp[i - 1][j], dp[i - 1][1] + 1, dp[i - 1][2] + 1)
            elif j == 1:
                cur_min = min(dp[i - 1][j], dp[i - 1][0] + 1, dp[i - 1][2] + 1)
            else:
                cur_min = min(dp[i - 1][j], dp[i - 1][0] + 1, dp[i - 1][1] + 1)
            dp[i][j] = cur_min
print(dp)
print(min(dp[n - 1]))