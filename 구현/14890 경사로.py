def set_slide(row, col, dy, dx):
    if dy >= 0 and dx >= 0:
        y, x = row + dy, col + dx
    else:
        y, x = row, col

    height = field[y][x]
    potential = []  # 방문 즉시 경사로 놓으면 안되고 일단 수집해야 됨(이후 셀에서 경사로 못놓는 상황 발생가능)
    for _ in range(slide_len):
        if not (0 <= y < line_len and 0 <= x < line_len):
            return False
        if already_slide[y][x] or field[y][x] != height:
            return False
        potential.append((y, x))
        y += dy
        x += dx

    for y, x in potential:  # return False 안하고 여기 왔다면 경사로 설치 가능하다는 뜻
        already_slide[y][x] = True  # 그럼 그땐 실제로 경사로 설치
    return True


def line_search(dy, dx):
    global slide_cnt
    fail = False

    for i in range(line_len):
        for j in range(line_len - 1):  # IndexError 때문에 끝에서 하나 모자를 때까지 진행
            if dy == 0:
                row, col = i, j  # 행방향 길 탐색: row 고정 후 col 탐색
            else:
                row, col = j, i  # 열방향 길 탐색: col 고정 후 row 탐색

            cur, next = field[row][col], field[row + dy][col + dx]
            if cur != next:  # 현재와 다음칸 같으면 그냥 진행, 다르면 뭔가 조치
                if abs(cur - next) > 1:  # 다르면 높이차 1 차이만 허용, 그거 초과는 바로 실패
                    fail = True
                    break
                else:  # 높이차 1
                    ty = -dy if cur < next else dy  # 현재 칸보다 다음 칸이 더 높으면 역방향 경사로
                    tx = -dx if cur < next else dx
                    if not set_slide(row, col, ty, tx):
                        fail = True
                        break

        if not fail:
            slide_cnt += 1  # 끝에 도달 시 성공 집계
        fail = False


line_len, slide_len = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(line_len)]

slide_cnt = 0
already_slide = [[False] * line_len for _ in range(line_len)]
line_search(0, 1)
already_slide = [[False] * line_len for _ in range(line_len)]  # row방향 탐색때 더럽혀졌으므로 초기화
line_search(1, 0)
print(slide_cnt)







# `````````````````````````````````````
# 개선 코드: line_search가 닉값 하도록, 전체 셀이 아닌 특정 한개의 라인 탐색만 담당하게 함

line_len, slide_len = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(line_len)]
slide_cnt = 0
already_slide = [[False] * line_len for _ in range(line_len)]


def set_slide(row, col, dy, dx):
    global already_slide, field
    height = field[row][col]
    potential_slides = []

    for _ in range(slide_len):
        if not (0 <= row < line_len and 0 <= col < line_len) or already_slide[row][col] or field[row][col] != height:
            return False
        potential_slides.append((row, col))
        row += dy
        col += dx

    for row, col in potential_slides:
        already_slide[row][col] = True
    return True


def line_search(index, dy, dx):
    global slide_cnt, field
    fail = False
    for j in range(line_len - 1):
        row, col = (index, j) if dy == 0 else (j, index)
        cur, next = field[row][col], field[row + dy][col + dx]
        if cur != next:
            if abs(cur - next) > 1:
                fail = True
                break
            else:
                ty, tx = (-dy, -dx) if cur < next else (dy, dx)
                slide_start_row, slide_start_col = (row - ty, col - tx) if cur < next else (row, col)
                if not set_slide(slide_start_row, slide_start_col, ty, tx):
                    fail = True
                    break
    if not fail:
        slide_cnt += 1


for i in range(line_len):
    line_search(i, 0, 1)

already_slide = [[False] * line_len for _ in range(line_len)]

for i in range(line_len):
    line_search(i, 1, 0)

print(slide_cnt)
