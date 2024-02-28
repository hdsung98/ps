# [비효율적인 풀이]

import sys

input = lambda: sys.stdin.readline().rstrip()


def calc(commmand, nums):
    for com in commmand:
        if com == 'R':
            nums = nums[::-1]
        elif com == 'D':
            if nums:
                nums = nums[1:]
            else:
                print('error')
                return
    print(list(map(int, nums)))


test_case = int(input())
for _ in range(test_case):
    commands = list(input()) # 루프마다 임시로 받고 덮어써버리자
    cnt = int(input())
    list_input = input()[1:-1]

    # num_list = []
    # if cnt == 0:
    #     input() # 이걸 누락했다. 인풋은 어떤경우에도 고정적으로 받아야되는데 직무유기 발생
    #     pass
    # else:
    #     for w in input()[1:-1].split(','): # SPLIT은 DELIM 문자는 지워버리고 파싱한다. 굳이 ISDIGIT 불필요. 이미 다 숫자
    #         if w.isdigit():
    #             num_list.append(w)
    if cnt > 0:
        num_list = list(map(int, list_input.split(',')))
    else:
        num_list = []

    calc(commands, num_list)

# ````````````````````````````````````
# [효율적인 풀이: reverse는 절대 직접 뒤집으면 안된다]
import sys

input = lambda: sys.stdin.readline().strip()


def calc(commands, nums):
    reverse = False
    for com in commands:
        if com == 'R':
            reverse = not reverse  # 연산 뒤집기!
        elif com == 'D':
            if len(nums) == 0:
                print('error')
                return
            if reverse:
                nums.pop()
            else:
                nums.pop(0)
    if reverse:
        nums.reverse() # 최종 결과가 reverse면 한번 뒤집어줘야함
                       # reverse는 mutable에만 적용(리스트는 가능, 문자열은 불가)
    print("[" + ','.join(map(str, nums)) + "]") # map은 iterable을 받아 iterable을 리턴


test_case = int(input())
for _ in range(test_case):
    commands = list(input())
    cnt = int(input())
    list_input = input()[1:-1] # cnt가 0인가와 무관하게 입력은 일단 받기
    if cnt > 0:
        nums = list(map(int,list_input.split(','))) # 스플릿은 공백에 사용하면 안된다
                                                    # 입력은 문자열이었다 형변환까먹지 말자
    else:
        nums = []
    calc(commands, nums)


