first, second = list(input()), list(input())
len_f, len_s = len(first), len(second)
# dp 설계: dp[첫 문자열에서 몇번째 문자까지 고려했나][두번째 문자열에서 몇번째 문자까지 고려했나]
# 0행 및 0열은 한쪽 문자열을 통째로 고려하지않은 경우이므로
# 문자를 하나라도 고려하기 시작하면 +1한 인덱스에 dp 정보 넣어줘야함
dp = [[0] * (len_f + 1) for _ in range(len_s + 1)]

for i in range(len_s):
    for j in range(len_f):
        if first[j] == second[i]: # 현재 문자가 일치!
            dp[i + 1][j + 1] = dp[i][j] + 1  # 두 문자의 직전 레벨 최적값 + 이번에 일치한 문자 1개
        else: # 현재 문자 불일치
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) # 현재 문자는 고려 못하니, 이전 단계 중 최적 선택

print(dp[len_s][len_f])
