expression = list(input())
num = ""
num_list = []
op_list = []
for ch in expression:
    if ch.isdigit():
        num += ch
    else:
        num_list.append(int(num))
        op_list.append(ch)
        num = ""

if num:
    num_list.append(int(num))

result = num_list[0]
in_bracket = 0
for idx, op in enumerate(op_list):
    if op == '-':
        if in_bracket != 0:
            result -= in_bracket
            in_bracket = 0
        in_bracket += num_list[idx + 1]
    elif op == '+':
        if in_bracket == 0:
            result += num_list[idx + 1]
        else:
            in_bracket += num_list[idx + 1]

if in_bracket > 0:
    result -= in_bracket

print(result)

#----------------------------------------------
# 최적화 풀이

expression = input().split('-') # 뺄셈을 기준으로 분리.
num_list = []

for part in expression:
    temp_sum = sum(map(int, part.split('+'))) # 한 -에서 다음-까지를 내를 하나의 괄호영역으로 보고 각 구간을 더함
    num_list.append(temp_sum)

result = num_list[0] - sum(num_list[1:])
print(result)
