from itertools import *

perm = list(permutations(range(1, 10), 3))

n = int(input())
guess = []
possible = []
for _ in range(n):
    g, s, b = map(int, input().split())
    guess = [int(i) for i in str(g)] # 형변환 주의
    for i, case_val in enumerate(perm): # perm의 값을 내부 순환동안은 업데이트해줘도 loop가 초기화되지않음
        case_s = case_b = 0
        for j in range(3):
            if guess[j] == case_val[j]:
                case_s += 1
            elif guess[j] in case_val:
                case_b += 1
        if case_s == s and case_b == b:
            possible.append(case_val)
    perm = possible # 새로운 범주에서 nested loop 실행
    possible = [] # nested loop 내에서 목적 다했으면 빠져나와서 초기화
print(len(perm))
