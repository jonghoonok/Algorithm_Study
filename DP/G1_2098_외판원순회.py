# 현재 위치, 방문한 기록
def travel(start, visit):
    # 모든 도시를 다 순회했다면
    if visit == check:
        # 마지막 도시에서 출발 도시로 돌아가는 길이 있다면 값을, 아니면 INF 리턴
        return cost[start][0] or INF

    # 이미 해당 출발점에 대해 계산이 이루어졌다면 바로 리턴: 중복 제거
    if dp[start][visit] is not None:
        return dp[start][visit]

    temp = INF
    for i in range(n):
        # i로 가는 길이 존재하고, 아직 방문하지 않았다면
        if cost[start][i] and visit & (1<<i) == 0:
            temp = min(temp, travel(i, visit|(1<<i))+cost[start][i])
    # 현재 위치와 현재까지 방문한 목록에 대응되는 최솟값을 갱신
    dp[start][visit] = temp

    return temp


n = int(input())
INF = 1000000*16
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))


check = (1<<n) - 1  # 모든 도시를 방문했을 때 visit의 값

# i번째로 방문한 도시에 대해 모든 경우의 수에서의 최소 비용을 저장
dp = [[None]*(1<<n) for i in range(n)]
# 0번 도시를 출발점으로 하여 출발
ans = travel(0, 1<<0)

print(ans)