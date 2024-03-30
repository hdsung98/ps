# 문제
# 아래와 같이 좌우로 N개의 장소가 있다.
# 장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다. 또, 다른 한 장소를 골라서 벌통을 둔다.

# 두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
# 각 장소에 적힌 숫자는 벌이 지나가면서 꿀을 딸 수 있는 양이다.
# 두 마리가 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀을 딴다. (벌통이 있는 장소에서도 같다.)
# 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
# 장소들의 꿀 양을 입력으로 받아 벌들이 딸 수 있는 가능한 최대의 꿀의 양을 계산하는 프로그램을 작성하라.

# 입력
# 첫 번째 줄에 장소의 수 N이 주어진다.
# 다음 줄에 왼쪽부터 각 장소에서 꿀을 딸 수 있는 양이 공백 하나씩을 사이에 두고 주어진다.

# 출력
# 첫 번째 줄에 가능한 최대의 꿀의 양을 출력한다.

# 제한
# 3 <= N <= 100~000
# 각 장소의 꿀의 양은 1 이상 10000 이하의 정수이다.


def middle_honey():  # 벌 - 꿀통 - 벌 배치 케이스: 무조건 벌은 양쪽 끝에 있어야 최대한 많은 꿀을 모을 수 있음
    global acc_sum, size
    fix_sum = acc_sum[-2] - acc_sum[1]  # 양끝(벌 출발장소)을 제외한 범위의 누적합
    if size > 3:
        add_var = max(field[1:-2])  # 꿀통이 놓인 자리는 양쪽 벌이 둘다 수집하므로 한번 더 더해줌
    else:  # 엣지 케이스 (총 3개의 장소만 주어질 때)
        add_var = field[1]
    return fix_sum + add_var


def left_honey(bee_pos):  # 꿀통 - 벌 - 벌 배치 케이스 : 꿀통을 최좌측에 놓고 한 벌을 최우측에 놔야 누적합 최대
    global acc_sum, size
    fix_sum = acc_sum[-1]  # 모든 구간 누적합
    sub_var = field[-1] + field[bee_pos]  # 최우측 벌 입장: 본인 자리와 다른 벌 자리는 꿀 수집 못함
    add_var = acc_sum[bee_pos]  # 이동하는 벌 입장: 본인 기준 좌측은 다 수집 가능(누적합은 1-based)
    return (fix_sum - sub_var) + add_var


def right_honey(bee_pos):  # 벌 - 벌 - 꿀통 배치 케이스 : left-honey와 정반대
    global acc_sum, size
    fix_sum = acc_sum[-1]  # 모든 구간 누적합
    sub_var1 = field[0] + field[bee_pos]  # 최좌측 벌 입장: 본인 자리와 다른 벌 자리는 꿀 수집 못함
    sub_var2 = acc_sum[bee_pos + 1]  # 이동하는 벌 입장: 본인 자리 포함 좌측은 다 수집 불가능(누적합은 1-based)
    return (fix_sum - sub_var1) + (fix_sum - sub_var2)


size = int(input())
field = list(map(int, input().split()))
acc_sum = [0] * (size + 1)  # 1-based
for i in range(1, size + 1):
    acc_sum[i] = acc_sum[i - 1] + field[i - 1]  # field는 0-based

middle_max, left_max, right_max = middle_honey(), 0, 0
for i in range(1, size - 1):
    left_max = max(left_max, left_honey(i))
    right_max = max(right_max, right_honey(i))

print(max(left_max, middle_max, right_max))
