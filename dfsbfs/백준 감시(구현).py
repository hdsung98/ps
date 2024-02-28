# dir 선언
# 1~5 cctv 정의
# 회전 정의

right, left, up, down = [0, 1], [0, -1], [1, 0], [-1, 0]
cctv_dir = {
    1: [[right], [down], [left], [up]],
    2: [[right, left], [up, down]],
    3: [[right, up], [right, down], [left, down], [left, up]],
    4: [[right, up, left], [up, right, down], [right, down, left], [down, left, up]],
    5: [[right, down, left, up]]
}

h, w = map(int, input().split())
space = [[0] * w for _ in range(w)]
total_zero = 0
cctv_pos = []
for i in range(h):
    row = map(int, input().split())
    for j, num in enumerate(row):
        if num == 0:  # 입력받을때 0개수 계산
            total_zero += 1
        elif num < 6:
            cctv_pos.append((i, j, cctv_dir[num]))

# 회전시킬 조합을 모두 구하기
# 걔네 회전 시키기


# 회전된 cctv로 사각지대 계산
# visited 필요
# 사각지대 계산 함수(감시영역 개수 누적, space 업데이트 후 리턴)


# min 값 계산
