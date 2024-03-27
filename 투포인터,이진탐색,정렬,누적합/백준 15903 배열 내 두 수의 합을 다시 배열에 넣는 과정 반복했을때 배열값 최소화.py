import heapq

card_num, combine_num = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(combine_num):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    combine = a + b
    for _ in range(2): heapq.heappush(cards,combine)

print(sum(cards))
