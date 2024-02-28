import sys

input = sys.stdin.readline


def calc(stickers, col):
    dp = [[0] * 3 for _ in range(col)] # 테케, 스티커 열수가 어마어마하므로 dp로 풀어야됨.
    dp[0][0], dp[0][1], dp[0][2] = stickers[0][0], stickers[1][0], 0

    for i in range(1, col): # 독립적인 부분문제: 열별 선택
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + stickers[0][i] #윗칸 선택
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + stickers[1][i] # 아랫칸 선택
        dp[i][2] = max(dp[i - 1]) # 둘다 선택안함

    print(max(dp[col - 1]))


test_case = int(input().strip())
for _ in range(test_case):
    col = int(input().strip()) 
    stickers = [list(map(int, input().strip().split())) for _ in range(2)]
    calc(stickers, col)
