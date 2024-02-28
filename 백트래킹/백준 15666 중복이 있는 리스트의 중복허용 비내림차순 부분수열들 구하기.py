last, max_select = map(int, input().split())
input_list = sorted(list(map(int, input().split())))
seq = []
result_seq = []


def dfs(prev, cnt):
    # 뎁스간 중복허용(한뎁스 내에서의 중복은 여전히 불허) = range(start~~)안됨! 처음부터 다시 순회
    # 처음부터 다시 순회함에도 비내림차순해야됨! = 직전 원소의 값 보존했다가 비교할 필요 있음
    if cnt == max_select:
        print(' '.join(map(str, seq)))
        return

    used = set()
    for i in range(len(input_list)):
        cur = input_list[i]
        if cur in used or prev > cur:
            continue
        used.add(cur)
        seq.append(cur)
        dfs(cur, cnt + 1)
        seq.pop()


dfs(0, 0)
