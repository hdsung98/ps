# 문제
# 사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
#
# 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.
#
# 셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.
#
# N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 5
# 10 9
# 4 1 2 3 4
# 2 1 5
# 2 2 6
# 1 7
# 1 8
# 2 7 8
# 1 9
# 1 10
# 2 3 10
# 1 4
# 예제 출력 5
# 4

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        if root_x == truth_root:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


ppl_num, party_num = map(int, input().split())
parent = [i for i in range(ppl_num + 1)]
truth_ppl = list(map(int, input().split()))[1:]
truth_root = 0

if truth_ppl:
    for i in range(1, len(truth_ppl)):
        union(truth_ppl[0], truth_ppl[i])

parties = []
for _ in range(party_num):
    participant = list(map(int, input().split()))[1:]
    parties.append(participant[0])  # 어차피 파티원은 다 같은 그룹이 되므로 모든 멤버 다 추가할 필요 x
    for i in range(len(participant) - 1):
        union(participant[i], participant[i + 1])

cnt = 0
for party in parties:
    if find(party) != truth_root:
        cnt += 1
print(cnt)
