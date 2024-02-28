# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 예제 입력 1
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# 예제 출력 1
# ABDCEFG
# DBAECFG
# DBEGFCA

# 핵심: 시작점, 재귀순서, 바텀케이스만 설계하면 나머지는 재귀함수가 알아서한다


from collections import defaultdict

result1, result2, result3 = '', '', ''


def preorder(node):
    global result1

    if node == '.':
        return

    left, right = graph[node]
    result1 += node
    preorder(left)
    preorder(right)


def midorder(node):
    global result2
    if node == '.':
        return

    left, right = graph[node]
    midorder(left)
    result2 += node
    midorder(right)


def postorder(node):
    global result3

    if node == '.':
        return

    left, right = graph[node]
    postorder(left)
    postorder(right)
    result3 += node


graph = defaultdict(list)
for _ in range(int(input())):
    p, c1, c2 = input().split()
    graph[p] = [c1, c2]

preorder('A')
midorder('A')
postorder('A')
print(result1)
print(result2)
print(result3)


