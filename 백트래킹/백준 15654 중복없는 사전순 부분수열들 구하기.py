last, max_select = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()  # 사전순으로 증가해야하므로, 첫원소가 가장 작은 것이어야한다. 고로 정렬.
seq = []


def dfs(start, selected):
    if selected == max_select:
        print(' '.join(map(str, seq)))
        return

    for i in range(len(input_list)):  # 오름차순일 필요 없으므로 range의 시작 파라미터에 start 미삽입
        cur = input_list[i]
        if cur not in seq:  # 대신 중복은 허용하지 않으므로 not in 활용
            seq.append(cur)
            dfs(i + 1, selected + 1)
            seq.pop()


dfs(0, 0)
