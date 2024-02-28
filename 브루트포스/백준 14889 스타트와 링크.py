from itertools import *


def calc(team):
    result = 0
    pair = combinations(team, 2)
    for n1, n2 in pair:
        result += s[n1][n2] + s[n2][n1]
    return result


num = int(input())
s = [list(map(int, input().split())) for _ in range(num)]

min_diff = float("inf")
sum1 = 0
sum2 = 0

total_member = [i for i in range(num)]
team_combs = combinations(total_member, int(num / 2))
for team in team_combs:
    team1 = list(team)
    team2 = [member for member in total_member if member not in team1]
    # 리스트간 뺄셈 = set으로 형변환

    sum1 = calc(team1)
    sum2 = calc(team2)
    cur_diff = abs(sum1 - sum2)
    if min_diff > cur_diff:
        min_diff = cur_diff

print(min_diff)
