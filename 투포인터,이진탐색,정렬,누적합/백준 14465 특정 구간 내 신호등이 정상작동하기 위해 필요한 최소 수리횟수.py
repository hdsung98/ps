# 문제
# 1번부터 N번까지의 번호가 붙은 신호등 N (1 ≤ N ≤ 100,000)이 있다.
# 그러던 어느 날, 강력한 뇌우로 인해 몇몇 신호등이 망가졌다.
# 존은 연속한 K개의 신호등이 존재하도록 신호등을 수리하고 싶다.

# 입력
# 첫 줄에 N, K, B (1 ≤ B,K ≤ N)가 주어진다. 그 다음 B줄에는 고장난 신호등의 번호가 하나씩 주어진다.

# 출력
# 정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지 출력한다.

# 예제 입력 1
# 10 6 5
# 2
# 10
# 1
# 5
# 9
# 예제 출력 1
# 1

# 발상의 전환
    # [BAD] 브루트 포스: 고칠 신호등을 골라 그때 연속인 신호등 구간이 K를 넘는게 있는지 조사
    #                    (몇개를 고칠지 어느걸 고칠지, K개연속인 구간이 있는지 죄다 구해야함)
    # [GOOD] 누적합+슬라이딩 윈도우: 구간 길이 K를 고정시키고 이동시키며, 해당 구간을 연속되게 만드려면 신호등 몇개를 고쳐야하는지 계산. O(N)에 끝냄
# 슬라이딩 윈도우 사용 근거: 고정된 구간에 대한 문제이므로
# 누적합 사용 근거: 특정 구간 내 원소에 대한 반복적인 연산 필요한 경우

total, k, broken = map(int, input().split())

arr = [0] + [1] * total
for _ in range(broken):
    arr[int(input())] = 0
for i in range(1, total + 1):
    arr[i] += arr[i - 1]

start, end = 0, k
min_fix = float('inf')
while end <= total:
    normal = arr[end] - arr[start]
    fix = k - normal
    min_fix = min(min_fix, fix)

    start += 1
    end += 1

print(min_fix)
