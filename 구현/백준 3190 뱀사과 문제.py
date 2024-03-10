from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def change_dir(cur_dir, command):
    # if command == 'L':
    #     return (cur_dir - 1) % 4
    # elif command == 'D':
    #     return (cur_dir + 1) % 4
    dir_delta = {'L': -1, 'D': 1}  # 상황에 따른 가중치가 있다면, 조건분기보다 딕셔너리가 가독성 굿
    return (cur_dir + dir_delta[command]) % 4


board_size = int(input())
# apples = set()
# for _ in range(int(input())):
#     apples.add(tuple(map(lambda x: int(x) - 1, input().split())))
apples = {tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(int(input()))}

# moves = {}
# for _ in range(int(input())):
#     input_string = input().split()
#     time, move = int(input_string[0]), input_string[1]
#     moves[time] = move
moves = {int(time): move for time, move in (input().split() for _ in range(int(input())))}
time_to_move = moves.keys()

snake_head = (0, 0)
current_direction = 0
time_passed = 0
snake_body = deque([snake_head])  # 방문처리된 공간이 곧 뱀의 길이, 머리꼬리 모두 pop가능해야하므로 덱이 적절

while True:
    time_passed += 1
    dy, dx = dir[current_direction]
    snake_head = (snake_head[0] + dy, snake_head[1] + dx)  # 현 좌표를 여러번 써야한다면 튜플로 관리

    if not (0 <= snake_head[0] < board_size and 0 <= snake_head[1] < board_size) \
            or snake_head in snake_body:
        print(time_passed)
        exit(0)

    snake_body.append(snake_head)
    if snake_head in apples:
        apples.discard(snake_head)  # 셋 원소 제거 옵션은 discard나 remove가 있는데, discard는 해당 값이 셋에 없어도 에러 x
    else:
        snake_body.popleft()  # 덱을 쓴 목적!

    if time_passed in moves:
        current_direction = change_dir(current_direction, moves[time_passed])
