import sys
from collections import defaultdict

input = sys.stdin.readline


def count_target(target, start, end):
    # start,end는 0-based
    global dict
    if target not in dict or start > end:
        return 0
    return dict[target][end + 1] - dict[target][start]
    # dict는 1-based이므로
    # end+1이 실제 end를 가리키는 것, start는 실제 start 한칸 전


word = input().strip()  # 문자열 자체가 sequence. list로 바꿀 필요 없다
dict = defaultdict(lambda: [0] * (len(word) + 1))  # 더미 인덱스 0을 추가하면, 누적합 구하고 구간합 계산할 때 예외처리 적어짐

for c in set(word):
    for i in range(1, len(word) + 1):  # dict는 1-based, word는 입력된 문자열 그 자체이므로 0-based
        dict[c][i] = dict[c][i - 1] + (word[i - 1] == c)  # 불리언 값은 수식 내에서 0,1로 해석 됨!

for _ in range(int(input())):
    target, start, end = map(str, input().strip().split())
    print(count_target(target, int(start), int(end)))
