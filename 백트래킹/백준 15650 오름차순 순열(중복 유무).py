last, max_select = map(int, input().split())
seq = []


def dfs(start, selected):
    if selected == max_select:
        print(' '.join(map(str, seq)))
        return

    for n in range(start, last + 1):
        seq.append(n)
        dfs(n, selected + 1)  # 이건 중복있음. n"+1"로 하면 n보다 1 큰수부터 다음 수를 append하므로 중복x
        seq.pop()


dfs(1, 0)
