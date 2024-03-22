import sys
def initialize(n):
    global parent, rank
    parent = list(range(n))
    rank = [0] * n


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return False
    else:
        return True

input = sys.stdin.readline

dot_num, round_num = map(int, input().strip().split())
initialize(dot_num)

for i in range(round_num):
    start, end = map(int, input().strip().split())
    if union(start, end):
        print(i + 1)
        exit()

print(0)
