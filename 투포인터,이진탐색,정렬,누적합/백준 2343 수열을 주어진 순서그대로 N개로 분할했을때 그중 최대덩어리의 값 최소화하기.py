# 문제
# N개의 강의를 최대 M개의 블루레이에 순서대로 녹화할 때,
# 모든 블루레이의 크기(녹화 가능한 최대 길이)를 같게 하면서 그 크기의 최소값을 구하는 프로그램을 작성한다.
# 강의의 순서는 바뀌면 안 된다.

# 입력
# 첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다.
# 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다.
# 각 강의의 길이는 10,000분을 넘지 않는다.

# 출력
# 첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.

# 예제 입력 1
# 9 3
# 1 2 3 4 5 6 7 8 9
# 예제 출력 1
# 17

# ------------------------------------------------
# 모든 분할 경우의 수를 구하는 것은 매우 비효율적.
# 구하고자하는 것(블루레이 최대 길이 "최소값")을 탐색의 범위로 잡고
# 이를 이진 탐색으로 정답에 수렴시키며 찾는 것이 효과적.


def try_divide(capacity):
    part_len, video_num = 0, 1

    for i in range(seq_len):
        cur_len = part_len + seq[i]
        if cur_len > capacity:
            part_len = 0
            video_num += 1
        part_len += seq[i]

    # 목표치보다 적은 수로 분할되도 성공으로 간주하는 이유: 목표달성에 "여유"가 있음(사실상 성공)
    # ex) 3개 분할이 목푠데 이 길이로 2개로 분할도 된다? 그럼 3개로 굳이 쪼개 담는 것도 가능함
    # 따라서 "목표치달성 + 목표치보다 여유있는 케이스"를 성공으로 간주
    return video_num <= max_video_num


seq_len, max_video_num = map(int, input().split())
seq = list(map(int, input().split()))

min_len, max_len = max(seq), sum(seq)
perfect_len = max_len
while min_len <= max_len:  # 이진탐색은 결국 특정 값에 수렴할 때 종료된다.
    target_len = (min_len + max_len) // 2
    if try_divide(target_len):  # 결정문제화: 구하고자하는 것(최소 블루레이길이)로 조건만족할 수 있는가(M개이하로 분할) 체크
        perfect_len = target_len  # 따라서 찾고자하는 값을 min,max따위로 구하는게 아니다.
                                  # 루프의 마지막 순회에서 구한 값이 수렴값이고 그게 최적값

        max_len = target_len - 1  # 최소값을 찾을 때는, 조건만족 시 상방을 줄여 작은 범위를 탐색
    else:
        min_len = target_len + 1

print(perfect_len)


# -----------------------------------------------------------
# 잘못된 풀이

def try_divide(capacity):
    part_len, video_num = 0, 1

    for i in range(seq_len):
        cur_len = part_len + seq[i]
        if cur_len < capacity:
            part_len += seq[i]
        elif cur_len > capacity:
            part_len = seq[i]
            video_num += 1
        else:
            part_len = 0
            if i != seq_len - 1:
                video_num += 1

        if video_num > max_video_num:
            return 1

    if video_num < max_video_num:
        return 0
    else:
        return 2


seq_len, max_video_num = map(int, input().split())
seq = list(map(int, input().split()))

min_len, max_len = max(seq), sum(seq)
perfect_len = max_len
while min_len <= max_len:
    target_len = (min_len + max_len) // 2
    result = try_divide(target_len)
    if result == 0:
        max_len = target_len - 1
    elif result == 1:
        min_len = target_len + 1
    elif result == 2:
        perfect_len = min(perfect_len, target_len)
        max_len = target_len - 1

print(perfect_len)
