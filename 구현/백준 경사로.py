#
# streak = [[False] * size for _ in range(2)]
# row_max = [[0, 0, 0] for _ in range(size)]
# col_max = [[0, 0, 0] for _ in range(size)]
#
# for i in range(size):
#     change = False
#     max_cell = [0, 0, 0]
#     for j in range(size - 1):
#         cur_cell = board[i][j]
#         next_cell = board[i][j + 1]
#
#         if max_cell[2] < cur_cell:
#             max_cell = [i, j, cur_cell]
#         if cur_cell != next_cell:
#             change = True
#
#     row_max[i] = max_cell
#     if not change:
#         streak[0][i] = True
#
# for j in range(size):
#     change = False
#     max_cell = [0, 0, 0]
#     for i in range(size - 1):
#         cur_cell = board[i][j]
#         next_cell = board[i + 1][j]
#
#         if max_cell[2] < cur_cell:
#             max_cell = [i, j, cur_cell]
#         if cur_cell != next_cell:
#             change = True
#             print("change: ", i, j)
#
#     col_max[j] = max_cell
#     if not change:
#         streak[1][j] = True
#
# for i in range(size):
#     if streak[0][i]:
#         continue
#
#     my, mx, mv = row_max[i]
#     success = True
#     for j in range(mx, 0, -1):
#         cur_v = board[i][j]
#         next_v = board[i][j - 1]
#
#         slide_cnt = 0
#         if cur_v == next_v:
#             slide_cnt += 1
#             if slide_cnt == slide_len:
#                 slide_cnt = 0
#         elif abs(cur_v - next_v) > 1:
#             break

size, slide_len = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(size)]


def calc(line_num, dir):
    dy, dx = 0, 0
    if dir == 'col':
        y, x = 0, line_num
        dy = 1
    else:
        y, x = line_num, 0
        dx = 1

    visited = [[False] * size for _ in range(size)]
    while True:
        cur = board[y][x]
        next = board[y + dy][x + dx]
        slide_created, slide_opposite = False, False
        if cur != next:
            if abs(cur - next) > 1:
                return False
            slide_created, sy, sx = True, dy, dx

            if cur < next:
                sy, sx, slide_opposite = -dy, -dx, True
                slide_cur = cur
            else:
                slide_cur = next

            ny,nx = y,x
            if not slide_opposite:
                ny, nx = y + sy, x + sx
                # print(line_num, dir, y,x,ny, nx,'!')
            slide_record = []
            visited[ny][nx] = True
            for _ in range(slide_len - 1):
                ny, nx = ny + sy, nx + sx
                if not (0 <= ny < size) or not (0 <= nx < size):
                    # print(ny,nx)
                    return False
                if visited[ny][nx]:
                    # print(line_num,dir,ny,nx)
                    return False
                slide_next = board[ny][nx]
                if slide_cur != slide_next:
                    # print("3")
                    return False
                # print(ny, nx,sy,sx)
                slide_record.append((ny, nx))

            for ny, nx in slide_record:
                visited[ny][nx] = True
                #print(ny,nx)
                # print(ny,nx)
        # if slide_created and not slide_opposite:  # 놓침
        #     if dir == 'col':
        #         y += slide_len
        #     else:
        #         x += slide_len
        y, x = y + dy, x + dx  # 놓침

        if (not (dir == 'col' and 0 <= y < size - 1)) and (not (dir == 'row' and 0 <= x < size - 1)):
            if dir == 'col':
                print(line_num, 'col strike')
            else:
                print(line_num, 'row strike')
            return True


line_cnt = 0
# calc(4, 'col')
# exit()
for l_num in range(size):
    if calc(l_num, 'col'):
        line_cnt += 1

    if calc(l_num, 'row'):
        line_cnt += 1

print(line_cnt)
