# 문제
# M×N 크기의 보드에서 K×K 크기의 체스판을 잘라낸다.
# 검은색과 흰색이 번갈아 칠해진 체스판 형태로 만들기 위해 다시 칠해야 하는 정사각형의 최소 개수를 구해야 한다.
# 체스판은 맨 왼쪽 위 칸이 흰색 또는 검은색이 될 수 있다.
# 변을 공유하는 두 개의 사각형은 반드시 다른 색으로 칠해져 있어야 한다.

# 입력
# 첫째 줄에 정수 N, M, K가 주어진다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
# B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

# 제한
# 1 ≤ N, M ≤ 2000
# 1 ≤ K ≤ min(N, M)

# 예제 입력 1
# 4 4 3
# BBBB
# BBBB
# BBBW
# BBWB
# 예제 출력 1
# 2

# --------------------------------------------
# 발상의 전환
    # [BAD] 이 박스에서 어느 칸을 바꿔야 체스판규칙을 만족할까?
    # [GOOD] 이 박스가 이 패턴(왼쪽끝 검은색 OR 흰색)이 되려면 바꿔야 될 애가 누구누구일까?(과정과 목표의 변경)
    #    => 구간에 대한 반복적인 연산 필요하므로 "구간합"

# 1. 알고리즘 선택: 누적합 = 데이터의 부분영역에 대한 반복적 집계가 필요하고, 데이터 업데이트가 거의 없는 경우
# 2. 누적합의 내용: 구하고자하는 것(해당 구간 내 색깔 변경횟수)을 누적합 배열 셀의 내용으로 지정
# 3. 구간 내 변경횟수는 어떻게 구하나? = 체스판의 색배치 경우의수는 딱 두가지. 그 두 시나리오와의 불일치 계산.

import sys

input = sys.stdin.readline


def calc_change(start_color):
    arr = [[0] * (col + 1) for _ in range(row + 1)]  # 누적합은 1-based

    for i in range(1, row + 1):  # 1-based니까 순회패턴도 늘 이런식
        for j in range(1, col + 1):
            if ((i + j) % 2 == 0 and board[i - 1][j - 1] != start_color) \
                    or ((i + j) % 2 != 0 and board[i - 1][j - 1] == start_color):
                # 실제 체스판은 0-based이므로 누적합보다 1 빠꾸
                arr[i][j] = 1

            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

    return arr


row, col, cut_len = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(row)]

bw_case = calc_change('B')
wb_case = calc_change('W')

least = float('inf')
for i in range(row):
    for j in range(col):
        ei, ej = i + cut_len, j + cut_len
        if ei <= row and ej <= col:
            bw_total = bw_case[ei][ej] - bw_case[i][ej] - bw_case[ei][j] + bw_case[i][j]
            wb_total = wb_case[ei][ej] - wb_case[i][ej] - wb_case[ei][j] + wb_case[i][j]
            least = min(least, bw_total, wb_total)  # 새로운 두개와 기존 최솟값 비교 방법!

print(least)
