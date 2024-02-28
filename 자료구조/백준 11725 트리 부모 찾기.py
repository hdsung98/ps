# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

node_num = int(input().strip())
dict = defaultdict(list)  # 'value'로 삼을 자료형을 파라미터로 넘김
# NxN 그래프로 표현하면 빈 셀도 많고 공간낭비 심함
for _ in range(node_num - 1):
    a, b = map(int, input().strip().split())
    dict[a].append(b)  # 부모-자식 신경쓰지말고 양방향 그래프로 우선 표현
    dict[b].append(a)

q = deque(dict[1])  # 루트노드에서 탐색 시작
visited = [False] * (node_num + 1)
visited[1] = True
parent = defaultdict(int)  # (자식:부모) 정보를 저장할 딕셔너리

while q:
    cur = q.popleft()
    visited[cur] = True
    for node in dict[cur]:
        if visited[node]:  # 위에서부터 내려오므로, 이미 방문한 노드라면 부모
            parent[cur] = node
        else:  # 그렇지 않다면 자식
            q.append(node)

sorted_parent = {k: parent[k] for k in sorted(parent)}  # 정렬..(사실 불필요)
for i in sorted_parent.values():
    print(i)

########################### 개선된 풀이 ###########################


from collections import defaultdict, deque
import sys

input = sys.stdin.readline

node_num = int(input().strip())
graph = defaultdict(list)  # `dict`는 내장 함수/클래스 이름이므로 변수 이름을 `graph`로 변경
for _ in range(node_num - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])  # 자식이 아닌 "부모"를 큐에 삽입!!!!!
visited = [False] * (node_num + 1)
visited[1] = True  # 항상 시작점은 방문처리!
parent = defaultdict(int)

while q:
    cur = q.popleft()
    for node in graph[cur]:
        if not visited[node]:  # 방문하지 않은 노드 즉 자식에 대해
            visited[node] = True
            parent[node] = cur  # 현재 노드를 방문한 노드의 부모로 설정
            q.append(node) # 이 자식노드를 이제 부모 삼아 그 자손들 탐색 시작

# 굳이 parent를 키값 기준으로 정렬할 것 없다..키값 순서대로 순회해버리면 그만
for i in range(2, node_num + 1):
    print(parent[i])


# 핵심 아이디어:
# 1) 연결리스트로 양방향 연결관계 표현
# 2) 루트에서부터 bfs로 탐색
# 3) 방문처리로 부모 재방문 방지 및 부모-자식관계 식별