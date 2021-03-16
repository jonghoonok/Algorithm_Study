import sys

n = int(input())
street = [[0]*3 for _ in range(n)]
for i in range(n):
    street[i][0], street[i][1], street[i][2] = map(int, sys.stdin.readline().split())

# 해당 인덱스까지 최소가 되는 비용의 합을 색깔별로 저장
cost = [[0]*3 for _ in range(n)]
cost[0] = street[0]
for i in range(n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + street[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + street[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + street[i][2]

print(min(cost[n-1]))