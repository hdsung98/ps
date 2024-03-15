from collections import deque


def find_possible_comb(depth, idx, group):  # itertools 안쓰고 직접 조합 구현
    if depth == node_num:  # 최초 depth값 ~ node_num-1값: 원하는 최대 길이
        return

    for node in range(idx, node_num + 1):
        group.append(node)
        combs.append(tuple(group))  # deepcopy를 하던 tuple로 하던, 하여간 값 복사를 해야됨.
                                    # 그냥 group을 append하면, 주소참조라 combs는 최종적으로 빈 리스트만 갖게됨
        find_possible_comb(depth + 1, node + 1, group)  # node+1이지 idx+1 아니다.
                                                        # 재귀 까면서 내려가는 것만 생각하지말고, 반복문을 도는 걸 고려해라.
                                                        # node는 증가하는데 idx는 해당 루프내에서 고정이라 오름차순을 유지할 수 없다.
        group.pop()


def is_connected(comb):
    if not comb:  # 엣지 케이스 항상 주의!
        return False

    q = deque([comb[0]])
    visited = {comb[0]}  # 어차피 모든 노드를 다 돌게 아니기 때문에 set으로 관리하는게 공간복잡도 상 효율적
    while q:
        cur = q.popleft()
        for next in comb:
            if next not in visited and next in graph[cur]:
                visited.add(next)
                q.append(next)

    return len(visited) == len(comb)


node_num = int(input())
town_population = [-1] + list(map(int, input().split()))
graph = {i + 1: list(map(int, input().split()))[1:] for i in range(node_num)}

combs = []
find_possible_comb(0, 1, [])
# 가능 조합을 브루트포스로 구하자. 노드 수가 맥시멈 10개라 안크다
# 두 그룹으로 분할하는 것을 dfs로 구현하기는 무리. 끝까지 찍고 돌아오니까..


min_gap = float('inf')
visited = {comb: False for comb in combs}  # 분할 케이스 중복 체크 방지
for group_a in combs:
    group_b = tuple(set(range(1, node_num + 1)) - set(group_a))
    if not visited[group_a]:
        if is_connected(group_a) and is_connected(group_b):
            sum_a = sum(town_population[node] for node in group_a)
            sum_b = sum(town_population[node] for node in group_b)
            min_gap = min(min_gap, abs(sum_a - sum_b))

print(min_gap if min_gap != float('inf') else -1) # 엣지 케이스 항상 주의
