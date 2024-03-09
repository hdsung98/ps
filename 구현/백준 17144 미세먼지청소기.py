# 직관 그대로 작성해라.. 먼지 좌표리스트만 갖고 해결하려하지말고, 실제 방 좌표를 업데이트해라
# 최대 2500셀이니까 일일히 순회해도 된다

row, col, time = map(int, input().split())
room, cleaner = [], []
up_wind_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
down_wind_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(row):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    for j in range(col):
        if tmp[j] == -1:
            cleaner.append((i, j))


def spread():
    new_dust = []
    for y in range(row):
        for x in range(col):
            if room[y][x] <= 0:
                continue
            spread_v, spread_cnt = room[y][x] // 5, 0
            for dy, dx in up_wind_dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < row and 0 <= nx < col and room[ny][nx] != -1:
                    new_dust.append((ny, nx, spread_v))
                    spread_cnt += 1
            new_dust.append((y, x, -spread_v * spread_cnt))

    for y, x, v in new_dust:
        room[y][x] += v


def wind(cleaner, wind_dir, up):
    y, x = cleaner
    for dy, dx in wind_dir:
        while True:
            ny, nx = y + dy, x + dx
            if (up and 0 <= ny <= cleaner[0] and 0 <= nx < col) \
                    or (not up and cleaner[0] <= ny < row and 0 <= nx < col):
                if room[ny][nx] > 0:
                    if room[y][x] != -1:
                        room[y][x] = room[ny][nx]
                    room[ny][nx] = 0
                y, x = ny, nx
            else:
                break


for _ in range(time):
    spread()
    wind(cleaner[0], up_wind_dir, True)
    wind(cleaner[1], down_wind_dir, False)


total = sum(sum(cell for cell in row if cell != -1) for row in room)
# total = 0
# for i in range(row):
#     for j in range(col):
#         if not room[i][j] == -1:
#             total += room[i][j]
print(total)
