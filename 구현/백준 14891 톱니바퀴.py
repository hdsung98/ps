from collections import deque

chains = deque([deque(map(int, list(input()))) for _ in range(4)])
# chain_num = int(input())
# chains = deque([deque(map(int, list(input()))) for _ in range(chain_num)])
rotates = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    rotates.append([a - 1, b])


def rotate(chain, dir):
    if dir == 1:
        chains[chain].appendleft(chains[chain].pop())
    elif dir == -1:
        chains[chain].append(chains[chain].popleft())


def propagate(cur, prop_dir, rot_dir):
    l_prop = cur > 0 and chains[cur][6] != chains[cur - 1][2]
    r_prop = cur < len(chains) - 1 and chains[cur][2] != chains[cur + 1][6]
    rotate(cur, rot_dir)

    if not 0 < cur < len(chains) - 1:
        return

    if prop_dir == -1 and l_prop:
        propagate(cur - 1, -1, -rot_dir)
    elif prop_dir == 1 and r_prop:
        propagate(cur + 1, 1, -rot_dir)


cnt = 1
for cur, dir in rotates:
    l_prop = cur > 0 and chains[cur][6] != chains[cur - 1][2]
    r_prop = cur < len(chains) - 1 and chains[cur][2] != chains[cur + 1][6]
    rotate(cur, dir)
    cnt += 1
    if l_prop:
        propagate(cur - 1, -1, -dir)
    if r_prop:
        propagate(cur + 1, 1, -dir)

print(chains[0][0] + chains[1][0] * 2 + chains[2][0] * 4 + chains[3][0] * 8)
# cnt = 0
# for i in range(chain_num):
#     if chains[i][0] == 1:
#         cnt += 1
# print(cnt)

