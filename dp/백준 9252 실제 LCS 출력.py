from collections import deque

string_a, string_b = list(input()), list(input())
len_a, len_b = len(string_a), len(string_b)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if string_a[i - 1] == string_b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

y, x = len_a, len_b
result = deque()  # 앞에다 갖다 붙이면 역정렬 불필요!
while y > 0 and x > 0:  # 역추적 로직 / dp 인덱스 0은 어떤 문자도 고려하지않았으므로 종료
    if string_a[y - 1] == string_b[x - 1]:  # 문자열과 dp의 인덱스차이가 1임을 고려
        result.appendleft(string_a[y - 1])
        x -= 1
        y -= 1  # 대각선 역추적
    elif dp[y][x - 1] > dp[y - 1][x]:
        x -= 1
    else:
        y -= 1

print(dp[len_a][len_b])
print(''.join(result))

# ``````````````````````````````````````````````````

# BETTER SOLUTION: 역정렬 없이 DP업데이트와 동시에 같이 실제 LCS도 구하는 방법

string_a, string_b = input(), input()
len_a, len_b = len(string_a), len(string_b)

dp = [[0] * (len_a + 1) for _ in range(len_b + 1)]
path = [[''] * (len_a + 1) for _ in range(len_b + 1)]

for i in range(1, len_b + 1):
    for j in range(1, len_a + 1):
        if string_b[i - 1] == string_a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = path[i - 1][j - 1] + string_b[i - 1]  # 경로를 DP업데이트 과정에서 같이 업데이트하는 풀이
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                path[i][j] = path[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
                path[i][j] = path[i][j - 1]

print(dp[len_b][len_a])
print(path[len_b][len_a])
