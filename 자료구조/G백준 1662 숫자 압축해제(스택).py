# 문제
# 압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다.
# K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 이 Q라는 문자열이 K번 반복된다는 뜻이다.
# 압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 압축된 문자열 S가 들어온다. S의 길이는 최대 50이다. 문자열은 (, ), 0-9사이의 숫자로만 들어온다.

# 출력
# 첫째 줄에 압축되지 않은 문자열의 길이를 출력한다. 이 값은 2,147,473,647 보다 작거나 같다.

# 예제 입력 1
# 33(562(71(9)))
# 예제 출력 1
# 19

# -----------------------------
# 좀 더 최적화 한 코드: 괄호에 속하지 않는 바깥숫자는 바로 최종 result에 반영
seq = list(input())
stack = []
result = 0

for pos, c in enumerate(seq):
    if c == '(':
        if stack:
            stack[-1][1] -= 1
        else:
            result -= 1
        stack.append([int(seq[pos - 1]), 0])  # 핵심 아이디어: 곱해줄 수 K와 그 괄호안 길이를 스택원소로
    elif c == ')':
        mult, length = stack.pop()
        if stack:
            stack[-1][1] += mult * length  # 핵심 아이디어2(중첩 괄호 상황처리): 현재괄호 압축해제 길이 결과를 바깥괄호에 인계
        else:
            result += mult * length
    else:
        if stack:
            stack[-1][1] += 1
        else:
            result += 1

print(result)

# ----------------------------------
# 이전 코드
seq = list(input())
stack = []
result = 0
for pos, c in enumerate(seq):
    if c == '(':
        if stack:
            stack[-1][1] -= 1
        stack.append([int(seq[pos - 1]), 0])
    elif c == ')':
        mult, length = stack.pop()
        stack[-1][1] += mult * length
    else:
        if stack:
            stack[-1][1] += 1
        else:
            stack.append([1, 1])

for _ in range(len(stack) - 1):
    mult, length = stack.pop()
    stack[-1][1] += mult * length
print(stack[0][0] * stack[0][1])
