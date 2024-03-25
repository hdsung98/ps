# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
#
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
#
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
#
# 예제 입력 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# 예제 출력 1
# 3
# 힌트
# 공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기를 3개 설치할 수 없다.

def build_ok(dist):
    cnt = 1
    last = seq[0]
    # 첫번째 집부터 시작해도 select_num만큼 설치 불가능하면 n번째 집부터 시작한들 불가능하고
    # n번째집부터 시작해도  select_num만큼 설치 가능하면 첫번째 집부터 시작해도 가능
    # 고로 첫번째 집에서 시작하고 이것만 고려해도 최적의 해 보장

    for i in range(1, seq_len):
        if seq[i] - last >= dist:
            last = seq[i]
            cnt += 1

    return cnt >= select_num  # 일단 다 설치해보고 목표 설치 개수 달성했는지 검증하는게 효과적


seq_len, select_num = map(int, input().split())
seq = sorted([int(input()) for i in range(seq_len)])
min_len, max_len = 1, seq[-1] - seq[0]
result = 0

while min_len <= max_len:
    try_len = (min_len + max_len) // 2
    if build_ok(try_len):
        # 좋은 관점: "구하고자 하는 것!!"(가장 가까운 원소간 거리의 최대값)을 탐색의 범위로 둠
        # 나쁜 관점: 원소 조합을 일일이 구해서 그 조합 별 가장 가까운 원소의 최대값을 간접적으로 도출
        # 이진 탐색, 파라미터 탐색은 "구하고자 하는 것을 탐색범위로 두고" 그 결정을 "모듈화"해라!!!
        result = try_len
        min_len = try_len + 1
    else:
        max_len = try_len - 1

print(result)

# -------------------------------------------------------
# 잘못된 접근

min_len, max_len = 1, seq[-1] - seq[0]
try_len = (min_len + max_len) // 2
if seq_len == 2 and select_num == 2:
    print(max_len)
    exit()

while min_len < max_len:
    fail = False
    print(min_len, max_len, try_len)
    for i in range(select_num - 2):
        # 이상한 전제: 양 끝 점은 포함하고 시작
        # 아쉬운 접근 : select_num개수만큼 설치 시도하려함
        # 차라리 주어진 간격으로 설치 쭉하고 그 설치개수가 select_num만큼인지 세는게 indexerror나 엣지케이스 고려안해도 되고 쉽고 직관적
        if i + 1 > seq_len:
            max_len = try_len - 1
            fail = True
            break
        if seq[i] + try_len > seq[-2]:  # 모든 점을 다 출발점으로 삼아보려하고 있다. 비효율적
            max_len = try_len - 1
            fail = True
            break

    if not fail:
        min_len = try_len + 1

    try_len = (max_len + min_len) // 2
print(try_len)
