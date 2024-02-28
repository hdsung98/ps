#
# parens = list(input().strip())
# stack = []
# total = 0
# while parens:
#     new = parens.pop(0)
#     print("-------")
#     print("new: ", new)
#     if not stack:
#         stack.append((new,))
#     else:
#         top = stack[-1]
#         print("top: ", top)
#         if top == '(':
#             if new == '(' or new == '[':
#                 stack.append(new)
#             elif new == ']':
#                 print("h", 0)
#                 exit()
#             else:
#                 if a_inner == 0:
#                     a_inner = 2
#                     print("a closed! empty", total, a_inner, b_inner)
#                 else:
#                     total += (a_inner + b_inner) * 2
#                     a_inner, b_inner = 0, 0
#                     print("a closed! contents", total, a_inner, b_inner)
#                 stack.pop()
#         elif top == '[':
#             if new == '(' or new == '[':
#                 stack.append(new)
#             elif new == ')':
#                 print("j", 0)
#                 exit()
#             else:
#                 if b_inner == 0:
#                     b_inner = 3
#                     print("b closed! empty", total, a_inner, b_inner)
#                 else:
#                     total += (a_inner + b_inner) * 3
#                     a_inner, b_inner = 0, 0
#                     print("b closed! contents", total, a_inner, b_inner)
#                 stack.pop()
#
# print(total)

# ```````````````````````````````````````````````
# 개선코드
# 1. 핵심: 스택에는 여는 괄호만 있고 그 괄호구간 내부 값에 책임이 있다
#  => 괄호와 구간 내의 누적값을 하나의 쌍으로 스택에 추가한다
#      ( 처음 추가할 때는 0을, 내부값 계산 이후에는 스택 탑 여는괄호에 계산결과 업데이트)
# 2. 딕셔너리,셋을 활용해 패턴매칭을 추상화함


parens = list(input().strip())
stack = []
open, close = {'(', '['}, {')', ']'}
pattern = {'(': ')', '[': ']'}
result = 0
while parens:
    new = parens.pop(0)
    if not stack:
        if new in close:  # 엣지 케이스
            print(0)
            exit()
        else:
            stack.append([new, 0])
        continue

    if new in open:
        stack.append([new, 0])
    else:
        top, acc = stack[-1]  # top 은 0이 아니라 -1!!
        if pattern[top] == new:
            stack.pop()
            weight = 2
            if top == '[':
                weight = 3

            tmp = 0
            if acc:
                tmp = acc * weight
            else:
                tmp = weight

            if stack:
                stack[-1][1] += tmp
            else:
                result += tmp
        else:
            print(0)
            exit()

print(result)
