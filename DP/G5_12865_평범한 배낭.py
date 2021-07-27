n, k = map(int, input().split())
baggages = []
for _ in range(n):
    w, v = map(int, input().split())
    baggages.append((w, v))

# i행 : 1번부터 i번까지의 짐을 가방에 넣을 수 있을 때 최대 value
# j열 : 무게제한이 j일 때 가방에 들어 있는 짐들의 최대 value
DP = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if baggages[i-1][0] <= j:                      # i번째 짐의 무게가 현재 허용중량보다 가벼운 경우
            DP[i][j] = max(
                DP[i-1][j - baggages[i-1][0]] + baggages[i-1][1],   # i번째 짐을 포함시킨 경우의 value
                DP[i-1][j]                                          # 포함시키지 않은 경우의 value
            )
        else:
            DP[i][j] = DP[i-1][j]

print(DP[-1][-1])