def dfs(v):
    visit[v] = 1

    for w in edges[v]:
        if not visit[w]:
            dfs(w)


n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    com1, com2 = map(int, input().split())
    edges[com1].append(com2)
    edges[com2].append(com1)

visit = [0]*(n+1)

dfs(1)

result = 0
for node in visit:
    if node: result+=1

print(result - 1)