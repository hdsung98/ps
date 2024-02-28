max, num = map(int, input().split())

seq = []


def dfs():
    if len(seq) == num:
        print(' '.join(map(str, seq)))
        return

    for i in range(1, max + 1): # 처음부터 재차 시작, 순서가 유의미
        if i in seq:
            continue # 중복방지

        seq.append(i) 
        dfs() # i가 해당위치에 존재하는 모든 경우의 수 탐색
        seq.pop() # i pop. 현재 i 위치에 다른 숫자 삽입하게 "백트래킹"(뎁스는 경우의 수 소진때까지 유지)


dfs()
