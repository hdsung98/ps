from collections import *
from itertools import *

size, max_alive = map(int, input().split())
city = [[0] * size for _ in range(size)]
houses, chickens = [], []

for i in range(size):
    row = list(map(int, input().split()))
    for k, val in enumerate(row):
        city[i][k] = val
        if val == 1:
            houses.append((i, k))
        elif val == 2:
            chickens.append((i, k))

alive_chickens = combinations(chickens, max_alive)


def city_chicken_dist(alive_chicken):
    city_dist = 0
    for hy, hx in houses:
        home_dist = float("inf")
        for cy, cx in alive_chicken:
            home_dist = min(home_dist, abs(hy - cy) + abs(hx - cx))
        city_dist += home_dist
    return city_dist


min_result = float("inf")
for alive in alive_chickens:
    cur_dist = city_chicken_dist(alive)
    min_result = min(min_result, cur_dist)

print(min_result)

# bfs를 쓸 때를 안 쓸 때 구분하는 기준 설정(치킨집 위치를 아니까 굳이 bfs로 안풀어도 되는 문제였음..)
# 중첩 bfs 활용 케이스
# 백트래킹 문제는 아닌듯.. nqueen 풀기
