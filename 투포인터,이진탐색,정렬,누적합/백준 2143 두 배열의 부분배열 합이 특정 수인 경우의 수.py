# 문제
# 한 배열 A[1], A[2], …, A[n]에 대해서,
# 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다.
# 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다.
# 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때,
# A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.
# T(=5) = A[1] + B[1] + B[2]
#       = A[1] + A[2] + B[1]
#       = A[2] + B[3]
#       = A[2] + A[3] + B[1]
#       = A[3] + B[1] + B[2]
#       = A[3] + A[4] + B[3]
#       = A[4] + B[2]

# 입력
# 첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다.
# 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고,
# 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다.
# 다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고,
# 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다.
# 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.

# 출력
# 첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.

# 예제 입력 1
# 5
# 4
# 1 3 1 2
# 3
# 1 3 2
# 예제 출력 1
# 7

from collections import defaultdict


def calc_acc_sum_comb(seq, seq_len):
    # 단순 O(N^2) 순회하는 이유
    # 특정 값을 찾고자 하는게 아니라 모든 부분합 경우의 수를 준비해야 함
    # (투포인터,이진탐색은 필연적으로 경우의 수 누락.. 완탐이 필요할땐 부적절)
    # 크기가 1000이라 N^2해봤자 백만임

    dict = defaultdict(int)  # 같은 누적합 값이 여러 조합 경우의 수로 구해질 수 있고, 접근속도도 빨라서 딕셔너리가 적절
    for i in range(seq_len):
        prev_acc = 0
        for j in range(i, seq_len):
            cur_acc = prev_acc + seq[j]
            dict[cur_acc] += 1
            prev_acc += seq[j]

    return dict


target = int(input())

len_a = int(input())
a = list(map(int, input().split()))
len_b = int(input())
b = list(map(int, input().split()))

result = 0
sum_comb_a = calc_acc_sum_comb(a, len_a)
sum_comb_b = calc_acc_sum_comb(b, len_b)

for a_v, a_cnt in sum_comb_a.items():
    remain = target - a_v
    if remain in sum_comb_b:  # 음수도 부분합 딕셔너리에 존재 가능하다(remain > 0 조건 불필요)
        result += a_cnt * sum_comb_b[remain]

print(result)
