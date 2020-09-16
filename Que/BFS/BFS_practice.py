'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 인접행렬 이용
def BFS(G, v):
    # 큐, 방문
    q = []
    visit = [0]*(V+1)

    # enQ(v), visit(v)
    q.append(v)
    visit[v] = 1
    print(v, end=" ")

    # 큐가 비어있지 않은 동안
    while q:
        # v = deQ()
        v = q.pop(0)
        
        for w in range(1, V+1):
            # v의 인접한 정점(w)중에서 방문하지 않은 정점이면
            if G[v][w] and not visit[w]:
                # enQ(w), 방문 처리
                q.append(w)
                visit[w] = 1
                print(w, end=" ")

# 인접리스트 이용
def BFS2(G, v):
    # 큐, 방문
    q = []
    visit = [0]*(V+1)

    # enQ(v), visit(v)
    q.append(v)
    visit[v] = 1
    print(v, end=" ")

    # 큐가 비어있지 않은 동안
    while q:
        # v = deQ()
        v = q.pop(0)
        
        for w in G[v]:
            # v의 인접한 정점(w)중에서 방문하지 않은 정점이면
            if not visit[w]:
                # enQ(w), 방문 처리
                q.append(w)
                visit[w] = visit[v] + 1
                print(w, end=" ")
    
    maxIndex = 0
    for i in range(1, V+1):
        if visit[maxIndex] < visit[i]:
            maxIndex = i
    print()
    print(maxIndex, visit[maxIndex]-1)

# 입력
V, E = map(int, input().split())
temp = list(map(int, input().split()))

# 인접행렬 작성
G = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    G[s][e] = 1
    G[e][s] = 1

# 인접리스트 작성
G2 = [[] for _ in range(V+1)]
for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    G2[s].append(e)
    G2[e].append(s)

# BFS(G, 1)
BFS2(G2, 1)