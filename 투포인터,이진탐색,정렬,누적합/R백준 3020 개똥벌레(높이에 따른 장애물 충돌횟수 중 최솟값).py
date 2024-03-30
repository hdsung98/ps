# 문제
# 개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다.
# 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수)
# 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.
# 이 개똥벌레는 장애물을 피하지 않는다.
# 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
# 동굴의 크기와 높이, 모든 장애물의 크기가 주어진다.
# 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
# 다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

# 출력
# 첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.

# 예제 입력 1
# 6 7
# 1
# 5
# 3
# 3
# 5
# 1
# 예제 출력 1
# 2 3

# ---------------------------------------------
# 핵심: 길이 N짜리 장애물은 N미만 높이에서 모두 충돌 = 높이를 기준으로 누적합
# 핵심2: 누적합은 키-값 관점으로 접근. KEY= 높이, VALUE= 충돌하는 장애물 개수
import sys

input = sys.stdin.readline


def calc_acc_sum(arr, size):
    acc_sum = [0] * (size + 1)
    for val in arr:
        acc_sum[val] += 1  # 일단 높이별 장애물 개수 수집
    for i in range(size - 1, 0, -1):
        acc_sum[i] += acc_sum[i + 1]  # 현 높이보다 작은 높이에 장애물 개수 누적합
    return acc_sum


length, height = map(int, input().split())
obstacles_up, obstacles_down = [], []

for i in range(length):
    if i % 2 == 0:
        obstacles_down.append(int(input()))
    else:
        obstacles_up.append(int(input()))

obstacles_up_sum = calc_acc_sum(obstacles_up, height)
obstacles_down_sum = calc_acc_sum(obstacles_down, height)

min_crash, cnt = float('inf'), 0
for h in range(1, height + 1):
    total_crash = obstacles_down_sum[h] + obstacles_up_sum[height - h + 1]
    if total_crash < min_crash:
        min_crash, cnt = total_crash, 1
    elif total_crash == min_crash:
        cnt += 1

print(min_crash, cnt)
