# 문제
# 초기에 n+1개의 집합
# {0}, {1}, {2}, ... , {n}이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
# 집합을 표현하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# n, m이 주어진다. 
# m은 입력으로 주어지는 연산의 개수이다. 다음 
# m개의 줄에는 각각의 연산이 주어진다. 합집합은 
# 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 
# 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
# 
# 출력
# 1로 시작하는 입력에 대해서 a와 b가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.

# 제한
# 1 ≤ n ≤ 1,000,000
# 1 ≤ m ≤ 100,000
# 0 ≤ a, b ≤ n
# a, b는 정수 a와 b는 같을 수도 있다.

# 예제 입력 1 
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
# 예제 출력 1 
# NO
# NO
# YES

import sys

input = sys.stdin.readline


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
        # 좌변: 거슬러 올라갈때 만나는 모든 상위노드
        # 우변: 최상단 루트
        # 종합 결론: 거슬러 올라가는 모든 상위노드의 부모를 루트로 만들어 경로단축!
    return parent[node]
    # 결론적으로 루트 값을 전파받는거임


def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root # 루트를 다른 루트의 자식으로 두면, 그 아래 노드들은 자연히 따라서 편입


n, op_num = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(op_num):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)

    elif command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
