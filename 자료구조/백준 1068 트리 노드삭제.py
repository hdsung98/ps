# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
#
# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
#
# 예를 들어, 다음과 같은 트리가 있다고 하자.
#
#
#
# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.
#
#
#
# 이제 리프 노드의 개수는 1개이다.
#
# 입력
# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.
#
# 출력
# 첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.


# 핵심 아이디어: delte노드부터 dfs를 시작하면 delete노드 본인제거가 불가능. 루트부터 시작해서 delete node에서 탐색 멈춰라

from collections import defaultdict

node_num = int(input())
root_info = list(map(int, input().split()))
delete_node = int(input())

dict = defaultdict(list)
for cur, parent in enumerate(root_info):
    if parent == -1:
        root = cur
    else:
        dict[parent].append(cur)

if delete_node == root:
    print(0)
    exit()

# DFS
leaf_cnt = 0


def dfs(cur): # 핵심 아이디어: delete 노드에서 거슬러 올라가는 것이 아니라, 루트에서 delete노드까지만 탐색!
    global leaf_cnt

    if not dict[cur] or (len(dict[cur]) == 1 and dict[cur][0] == delete_node):
        leaf_cnt += 1
        return

    for child in dict[cur]:
        if child != delete_node: # delete노드 만난순간 그 쪽으로는 뎁스 더 안늘림(자연스레 삭제효과)
            dfs(child)


dfs(root)
print(leaf_cnt)
