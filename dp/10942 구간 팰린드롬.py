import sys

input = sys.stdin.readline

num_len = int(input().strip())
nums = list(map(int, input().strip().split()))
dp = [[0] * num_len for _ in range(num_len)]
for i in range(num_len - 1):
    dp[i][i] = 1
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
dp[num_len - 1][num_len - 1] = 1

for center_a in range(num_len):
    center_b = center_a + 1
    for dist in range(1, num_len):
        start, end_odd, end_even = center_a - dist, center_a + dist, center_b + dist
        if start < 0 or end_odd > num_len - 1 or end_even > num_len -1:
            break

        if dp[start + 1][end_odd - 1] and nums[start] == nums[end_odd]:
            dp[start][end_odd] = 1
        if dp[start + 1][end_even - 1] and nums[start] == nums[end_even]:
            dp[start][end_even] = 1

for _ in range(int(input().strip())):
    # start, end_odd = map(lambda x: int(x) - 1, input().strip().split())
    # print(1 if dp[start][end_odd] else 0)
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
