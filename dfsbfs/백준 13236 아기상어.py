from collections import deque

size = int(input())
space = [[0] * size for _ in range(size)]
bs_pos = [0, 0]
bs_size = 2
total_fish = 0
# space = [list(map(int, input().split())) for _ in range(size)] : list comprehension. 검색함
for i in range(size):
    row = list(map(int, input().split()))
    for j in range(size):
        space[i][j] = row[j]
        if row[j] == 9:
            bs_pos = [i, j]
        elif row[j] != 0:
            total_fish += 1

q = deque([(bs_pos[0], bs_pos[1], 0)])
moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
visited = [[False] * size for _ in range(size)]
visited[bs_pos[0]][bs_pos[1]] = True
time = 0
ate = 0
ate_bool = False
while q:
    y, x, acc_mv = q.popleft()
    print(y,x,acc_mv)
    for mv in moves: # dy,dx로 나눠받아라
        next_y, next_x = y + mv[0], x + mv[1] #ny,nx로 표현해라
        if 0 <= next_y < size and 0 <= next_x < size and not visited[next_y][next_x]: # 범위에 0 포함할 것
            # print("moved: " + str(next_y) + " " + str(next_x))
            fish_size = space[next_y][next_x]
            if 0 < fish_size < bs_size:
                space[next_y][next_x] = 0
                ate += 1
                ate_bool = True

                print("ate: " + str(next_y) + " " + str(next_x))
                if ate == bs_size:
                    bs_size += 1
                    ate = 0

            visited[next_y][next_x] = True
            acc_mv += 1
            q.append((next_y, next_x, acc_mv))

            if ate_bool:
                time += acc_mv - 1
                ate_bool = False

print(time)



# 작은 팁
# 1. list comprehension: [list(map(int, input().split())) for _ in range(size)]
#  1) map은 iterable 객체, but 인덱스접근,슬라이싱 불가
#  2) 따라서 바로 list로 형변환하는 것이 일반적
#  3) mutable 개념
# 	(1) mutable(list,set,dict): 할당 시 메모리 주소 복사 / 한 변수의 값 변경시 자동으로 다른변수도 변경
# 	(2) immutable: " / 그러나 한 변수 새값 할당시 메모리 재할당 & 변경 이뤄짐.
# 	(3) mutable 내에 mutable(2차원): 바깥 리스트는 새 메모리, 내부 1차원 리스트는 기존 것 참조
#  4) deep copy vs shallow copy
# 	(1) shallow copy(slicing)
# 	(2) deep copy:
# 2. 이동방향 for문에서 dy,dx로 분배하기 / ny,nx로 표시하기
# 3. 범위 검증 시 0 포함
