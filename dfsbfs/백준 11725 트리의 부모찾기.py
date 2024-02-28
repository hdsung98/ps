
# 1트: 28분


node_num = int(input())
adj = [[0] * 3 for _ in range(node_num + 1)]
for _ in range(node_num - 1):
    n1, n2 = map(int, input().split())
    if n1 == 1 or n2 == 1:
        if n1 != 1:
            child = n1
        else:
            child = n2
        if adj[1][1] == 0:
            adj[1][1] = child
        else:
            adj[1][2] = child
        adj[child][0] = 1

    elif adj[n1][0] != 0 and adj[n2][0] == 0:
        if adj[n1][1] == 0:
            adj[n1][1] = n2
        else:
            adj[n1][2] = n2
        adj[n2][0] = n1

    elif adj[n2][0] != 0 and adj[n1][0] == 0:
        if adj[n2][1] == 0:
            adj[n2][1] = n1
        else:
            adj[n2][2] = n1
        adj[n1][0] = n2


for i in range(2, node_num + 1):
    print(adj[i][0])

# `````````````````````````
# 접근법(28분 소요)
# 1. 각 노드별로 [부모,좌자녀,우자녀]를 할당한 adj 리스트를 만들었다
# 2. 엣지가 주어지면,
#  1) 노드가 1인 경우는 나머지 노드를 자녀로 자동 확정
#  2) 그 외에는 부모가 있는 노드를 상위노드로 가정하고 상대노드를 자식으로 삼음
# 3. 그렇게 모든 엣지 정보를 다 adj 리스트에 반영하고 부모에 해당하는 0번인덱스만 쫙 출력
#
# 문제점(디버깅 및 포기까지 총 40분소요)
# 하위노드가 먼저 주어지는 경우, 노드간 상하를 결정할 수 없는데 이 케이스 대비가 전혀안됨.
#
# ````````````````````````
from collections import deque

node_num = int(input())
tree = [[] for _ in range(node_num + 1)]

for _ in range(node_num - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

parents = [0] * (node_num + 1)

queue = deque([1])
parents[1] = 1

while queue:
    node = queue.popleft()
    for child in tree[node]:
        if parents[child] == 0:
            parents[child] = node
            queue.append(child)

for i in range(2, node_num + 1):
    print(parents[i])

# 일반화된 접근법
# 0. 문제가 그래프 탐색과 관련이 깊은 경우 bfs를 우선 고려
# 1. 연결관계를 인접리스트 그래프로 표현 / 방문기록을 할 자료구조 하나 선언(초기화 값 0,음수등오로 지정)
# 2. 큐 선언 및 첫번째 탐색 대상 삽입
# 3. 루프 돌기
#  1) 현재 노드와 연결된 노드 모두에 대해
#  2) 방문여부 확인 및 업데이트
#  3) 방문 노드를 큐에 재차 추가해 추가 탐색 진행
