import sys

input = sys.stdin.readline


def calc_average(r1, c1, r2, c2):
    global acc_sum
    sum = acc_sum[r2][c2] - acc_sum[r1-1][c2] - acc_sum[r2][c1-1] + acc_sum[r1-1][c1-1]
    return sum // ((r2 - r1 + 1) * (c2 - c1 + 1))


row, col, q_num = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(row)]
acc_sum = [[0] * (col + 1) for _ in range(row + 1)]

for i in range(1, row + 1):
    for j in range(1, col + 1):
        acc_sum[i][j] = acc_sum[i - 1][j] + acc_sum[i][j - 1] + picture[i - 1][j - 1] - acc_sum[i - 1][j - 1]

for _ in range(q_num):
    r1, c1, r2, c2 = map(int, input().strip().split())
    print(calc_average(r1, c1, r2, c2))
