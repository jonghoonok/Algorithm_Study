# Pesudo
STACK s
visited[]
DFS(v):
    push(s, v)
    while not isEmpty(s):
        v = pop(s)
        if not visited[v]:
            visit(v)
            for each w in adjacency(v):
                if not visited[w]:
                    push(s, w)

# Python
def DFS(v):
    stack = []
    visit = []

    stack.append(v)
    
    while stack:
        v = stack.pop()
        if v not in visit:
            visit.append(v)
            # stack.extend(G[w]) 로 아래 두 줄 대체할 수 있음
            for w in adjavency[v]:
                stack.append(w)