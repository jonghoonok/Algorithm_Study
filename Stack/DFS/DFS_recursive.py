# Pseudo Code
visited = [False]*7
# G는 그래프, v는 시작점
def DFS_Recursive(G, v):

    visited[v] = True     # v 방문했다고 check

    for w in adjacency(G, v):
        if visited[w] != True:
            DFS_Recursive(G, w)

