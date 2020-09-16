# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# G는 그래프, v는 시작점
def DFS_Recursive(v):

    if visited[v]:
        pass
    else:
        visited[v] = 1     # v 방문했다고 check
        print(v, end = " ")

    for w in range(1, n+1):        
        if adjacency[v][w] == 1 and visited[w] == 0:
            DFS_Recursive(w)

def DFS_repitition(v):
    stack = []
    stack.append(v)
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1            
            for w in range(n+1):
                if adjacency[v][w] == 1:
                    stack.append(w)
            



n, e = map(int, input().split())
edge_list = list(map(int, input().split()))
adjacency = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

# 인접행렬 작성
for i in range(e):
    adjacency[edge_list[i*2]][edge_list[i*2+1]] = 1
    adjacency[edge_list[i*2+1]][edge_list[i*2]] = 1
DFS_Recursive(1)