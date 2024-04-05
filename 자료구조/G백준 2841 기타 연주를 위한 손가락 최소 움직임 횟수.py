# 문제
# 기타 6개 줄에 P개 프렛이 있을 때, 주어진 멜로디를 연주하기 위해 손가락을 최소 몇 번 움직여야 하는지 구하는 프로그램을 작성하시오.
# 멜로디 연주 시 높은 프렛을 누르려면 낮은 프렛을 떼지 않고 추가로 누를 수 있으나, 낮은 프렛을 누를 때는 높은 프렛을 떼어야 한다.

# 입력
# 첫째 줄에 멜로디에 포함되어 있는 음의 수 N과 한 줄에 있는 프렛의 수 P가 주어진다. (1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)
# 다음 N개 줄에는 멜로디의 한 음을 나타내는 두 정수가 주어진다.
# 첫 번째 정수는 줄의 번호이고 두 번째 정수는 그 줄에서 눌러야 하는 프렛의 번호이다.
# 입력으로 주어진 음의 순서대로 기타를 연주해야 한다.
# 줄의 번호는 N보다 작거나 같은 자연수이고, 프렛의 번호도 P보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 멜로디를 연주하는데 필요한 최소 손가락 움직임을 출력한다.

# 예제 입력 1
# 5 15
# 2 8
# 2 10
# 2 12
# 2 10
# 2 5
# 예제 출력 1
# 7

# ------------------
# 중요 아이디어 1: 지금 놔야되는 손가락 위치가 직전 손가락에 영향을 받으므로 LIFO "스택"
# 중요 아이디어 2: 줄은 서로 독립적이므로 별도의 스택 6개를 구성
# 중요 아이디어 3: 스택문제는
#               1) 탑에 어떤속성을 둘지 정하고,
#               2) 새 원소가 들어올때 TOP 속성을 유지하기 위한 POP,
#               3) 새속성 APPEND 3단계로 이루어짐


import sys

input = sys.stdin.readline

note_num, pret_num = map(int, input().split())
finger = {i: [] for i in range(1, 7)}
finger_move = 0
for _ in range(note_num):
    line, pret = map(int, input().split())
    stack = finger[line]
    while stack and stack[-1] > pret:  # simple rule 1: 치려는 음보다 스택 탑이 높으면 pop
        stack.pop()
        finger_move += 1
    if not stack or stack[-1] < pret:  # simple rule 2: 치려는 음보다 스택 탑이 낮으면 append
        stack.append(pret)
        finger_move += 1

print(finger_move)
# -----------------------------------
# 비효율적인 코드

import sys

input = sys.stdin.readline

note_num, pret_num = map(int, input().split())
finger = {i: [] for i in range(1, 7)}
finger_move = 0
for _ in range(note_num):
    line, pret = map(int, input().split())
    stack = finger[line]
    if stack:
        if stack[-1] > pret:
            while stack and stack[-1] > pret:
                stack.pop()
                finger_move += 1
            if not stack or stack[-1] < pret:
                stack.append(pret)
                finger_move += 1
        elif stack[-1] < pret:
            stack.append(pret)
            finger_move += 1
    else:
        stack.append(pret)
        finger_move += 1

print(finger_move)
