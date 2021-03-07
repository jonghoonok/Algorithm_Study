import sys
import heapq

n = int(input())
cards = []
for i in range(n):
    card = int(sys.stdin.readline())
    heapq.heappush(cards, card)

# 카드 중에 가장 작은 수를 계속 더하면 된다
result = 0
for i in range(n-1):    # 더하는 건 n-1번 수행됨
    add = heapq.heappop(cards) + heapq.heappop(cards)
    result += add
    heapq.heappush(cards, add)
print(result)