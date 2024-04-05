# 문제
# 올바른 괄호 쌍을 가진 수식에서 괄호 쌍을 제거하여 생성할 수 있는 서로 다른 식의 개수를 계산하는 프로그램을 작성하시오.
# 괄호는 항상 쌍으로 제거되어야 하며, 모든 가능한 괄호 제거 조합을 고려해야 합니다.

# 입력
# 첫째 줄에 음이 아닌 정수로 이루어진 수식이 주어진다.
# 이 수식은 괄호가 올바르게 쳐져있다. 숫자, '+', '*', '-', '/', '(', ')'로만 이루어져 있다.
# 수식의 길이는 최대 200이고, 괄호 쌍은 적어도 1개, 많아야 10개이다.

# 출력
# 올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력한다.

# 예제 입력 1
# (0/(0))
# 예제 출력 1
# (0/0)
# 0/(0)
# 0/0


from itertools import combinations

exp = input()
stack, pairs = [], []
for pos, ch in enumerate(exp):
    if ch == '(':
        stack.append(pos)
    elif ch == ')':
        pairs.append((stack.pop(), pos))

del_combs = []
for i in range(1, len(pairs) + 1):
    # combinations는 해당 갯수의 모든 가능조합을 담은 "iterator"를 리턴
    # for문을 통해 접근하는 combo는 "튜플"형태의 한가지 조합
    for combo in combinations(pairs, i):
        # 리스트 컴프리헨션 된 이중 반복문은 좌->우 방향으로 nested
        flattened = set([n for pair in combo for n in pair])
        del_combs.append(flattened)

result = []
for del_comb in del_combs:
    left_words = ""
    for pos, ch in enumerate(exp):
        if pos not in del_comb:
            left_words += ch
    result.append(left_words)

for words in sorted(set(result)):
    print(words)
