import heapq, sys

input = sys.stdin.readline

cards = []
for _ in range(int(input())):
    heapq.heappush(cards, int(input()))

total_comparison = 0
while cards:
    cur_comparison = heapq.heappop(cards)
    if cards:
        cur_comparison += heapq.heappop(cards)
        total_comparison += cur_comparison
        heapq.heappush(cards, cur_comparison)
        cur_comparison = 0


print(total_comparison)
