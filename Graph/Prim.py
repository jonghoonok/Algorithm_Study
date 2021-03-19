'''
7 11
0 5 60
0 1 32
0 2 31
0 6  51
1 2 21
2 4 46
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 1. 정점으로부터 연결된 간선 중 가중치 제일 작은 것 선택
# 2. 간선으로 연결된 트리로부터 연결된 간선 중 작은 것
def mst():
    total = 0       # 가중치의 합
    u = 0           # 시작점
    D[u] = 0        # 시작점의 가중치를 0으로 세팅

    for i in range(V):
        # 이 부분을 힙으로 바꾸면 visit이 필요없음
        minD = INF
        for v in range(V):
            if visit[v] == 0 and minD > D[v]:
                minD = D[v]
                u = v   # 출발점으로부터 가장 가중치 작은 것 선택

        # 방문처리
        visit[u] = 1
        total += adj[PI[u]][u]  # 현재노드와 그 부모노드의 거리
        
        # 인접한 정점 업데이트
        for v in range(V):
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] > D[v]:
                D[v] = adj[u][v]
                PI[v] = u



INF = float('inf')
V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]   # 인접행렬
D = [INF] * V                       # 가중치
PI = list(range(V))                 # 부모(자기자신)
visit = [0] * V                     # 방문여부

# 입력
for i in range(E):
    temp = list(map(int, input().split()))  # 시작, 끝, 가중치
    adj[temp[0]][temp[1]] = temp[2]
    adj[temp[1]][temp[0]] = temp[2]

print(mst())
