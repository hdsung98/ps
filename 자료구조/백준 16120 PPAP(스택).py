# 문제
# 주어진 문자열이 PPAP 문자열인지 판별하는 프로그램을 작성하시오.
# PPAP 문자열은 문자 'P'로 시작해, 문자열 내의 'P'를 'PPAP'로 치환하는 과정을 반복하여 만들 수 있습니다.

# 입력
# 첫 번째 줄에 문자열이 주어진다. 문자열은 대문자 알파벳 P와 A로만 이루어져 있으며, 문자열의 길이는 1 이상 1,000,000 이하이다.

# 출력
# 첫 번째 줄에 주어진 문자열이 PPAP 문자열이면 PPAP를, 아닌 경우 NP를 출력한다.

# 예제 입력 1
# PPPAPAP
# 예제 출력 1
# PPAP

# 예제 입력 2
# PPAPAPP
# 예제 출력 2
# NP

#----------------------------
# 내 솔루션 : PPAP가 발견되는 순간 첫 P만 남기고 뒤의 PAP를 삭제
string = input()
stack = []
for c in string:
    stack.append(c)
    if len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        for _ in range(3):
            stack.pop()

print("PPAP" if stack == ['P'] else "NP")

# -------------------------
# 다른 솔루션(스택성질에 더 집중): A가 발견되면 이 이전의 PP를 삭제. PPA를 날림
# 더 적절한 이유: 스택은 LIFO이므로 가장 최근에 들어온 순서부터 역방향으로 고려하는 것이 맞다

S = input().strip()
stack = []

for c in S:
    if c == 'P':
        stack.append(c)
    else:
        if len(stack) >= 2 and (len(stack) > 2 and stack[-2] == 'P' and stack[-3] == 'P'):
            stack.pop()
            stack.pop()
        else:
            print("NP")
            exit()

print("PPAP" if len(stack) == 1 else "NP")