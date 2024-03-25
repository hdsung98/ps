# 문제
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

# 입력
# 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

# 출력
# 좋은 수의 개수를 첫 번째 줄에 출력한다.

# 예제 입력 1
# 10
# 1 2 3 4 5 6 7 8 9 10
# 예제 출력 1
# 8
# 힌트
# 3,4,5,6,7,8,9,10은 좋다.

size = int(input())
nums = list(map(int, input().split()))
nums.sort()


if size < 3:
    print(0)
    exit()

cnt = 0
for i in range(size):
    start, end = 0, size - 1
    target = nums[i]

    while start < end:
        start += 1 if i == 0 else 0
        end -= 1 if i == size - 1 else 0

        cur = nums[start] + nums[end]
        if cur < target:
            start += 1
        elif cur > target:
            end -= 1
        else:
            cnt += 1
            break

print(cnt)
