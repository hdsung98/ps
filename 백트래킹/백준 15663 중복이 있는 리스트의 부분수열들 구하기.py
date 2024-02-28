last, max_select = map(int, input().split())
input_list = list(map(int, input().split()))  # 입력 수열 정렬하지 않음
seq = []
result_seq = []
used_before = [False] * last  # 이전 모든 뎁스에서 선택된 숫자를 관리


def dfs(cnt):
    if cnt == max_select:
        result_seq.append(tuple(seq))  # seq을 그대로 append하면 백트래킹때문에 출력 시 빈칸임..(주소를 append하는 듯)
        # 주의!! 여기서 문자열로 저장해놓고 dfs끝나고 정렬돌리면, 아스키 값 기반 정렬이라 의도치않은 정렬이됨..
        return

    used_this_depth = set()  # 현 뎁스에서 선택된 숫자를 기록
    for i in range(len(input_list)):  # 오름차순 아니어도 됨(모든 순열)
        cur = input_list[i]
        if cur in used_this_depth or used_before[i]:
            # 전건: 한 뎁스 내에선 중복 숫자 하나로 취급
            # 후건: range가 다음 뎁스에서 처음부터 도니까 전체 뎁스 상에서 숫자 중복 방지
            # (단, 애초에 input_list에서 중복이었던 것은 다른 숫자 취급됨)
            continue
        used_this_depth.add(cur)
        used_before[i] = True
        seq.append(cur)
        dfs(cnt + 1)
        used_before[i] = False
        seq.pop()


dfs(0)

for seq in sorted(result_seq):  # 사전순으로 정렬하여 출력 (주의!!!: 문자열상태가 아닌 숫자 상태로 정렬해야됨)
    print(' '.join(map(str, seq)))
