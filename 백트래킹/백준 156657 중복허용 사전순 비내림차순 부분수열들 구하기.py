last, max_select = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()  # 부분수열들의 나열은 사전순이니까 정렬
seq = []


def dfs(start, selected):
    if selected == max_select:
        print(' '.join(map(str, seq)))
        return

    for i in range(start, len(input_list)):  # 비내림차순이어야 하므로 시작원소 start로 제한
        seq.append(input_list[i])
        dfs(i, selected + 1)  # i로 두어 중복 허용
        seq.pop()


dfs(0, 0)
