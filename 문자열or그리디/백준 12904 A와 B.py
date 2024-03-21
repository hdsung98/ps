import sys
sys.setrecursionlimit(10**6)
s = input().strip()
t = input().strip()
t_len = len(t)


def decide(start):
    if len(start) == t_len:
        if start == t:
            return 1
        else:
            return 0
    case1 = start + "A"
    case2 = start[::-1] + "B"

    if decide(case1) == 1 or decide(case2) == 1:
        return 1
    else:
        return 0


print(decide(s))

# --- 위에거는 재귀라 시간초과 뜸. 작은 문자열로 큰 문자열을 만드는 것은 발산적.. 큰문자열을 작은문자열로 수렴시키는 접근법이 훨씬 효과적

s = list(input().strip())
t = list(input().strip())

while True:
    end = t.pop()
    if end == 'B':
        t = t[::-1]

    if len(t) == len(s):
        if t == s:
            print(1)
        else:
            print(0)
        break


