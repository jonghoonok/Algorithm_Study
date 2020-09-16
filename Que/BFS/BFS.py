# Pseudo
def BFS(G, v):                  # enQueue시 방문 처리하는 경우
    visited = [0]*(n+1)
    q = []

    q.append(v)
    visited[v] = 1

    while len(q) != 0:
        t = q.pop(0)            # deQueue
        for w in G[t]:
            if not visited[w]:
                q.append(w)     # enQueue
                # visited[w] = visited[t] +1    출발점으로부터의 depth를 알 수 있음
                visited[w] = 1

def BFS(G, v):                  # deQueue시 방문 처리하는 경우
    visited = [0]*(n+1)
    queue = []

    queue.append(v)
    
    while queue:
        t = queue.pop(0)        
        if not visited[t]:      # t에 방문한적 있으면 다음 노드로 넘어가고 아니면 인접 노드 추가
            visited[t] = 1
            for w in G[v]:
                queue.append(w)
