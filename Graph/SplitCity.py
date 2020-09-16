def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda a:a[2])

# 최소신장 트리 '내부에' 있는 간선 중에서 가장 비용이 큰 간선
last = 0
for edge in edges:
    if find_parent(edge[0]) != find_parent(edge[1]):
        result += edge[2]
        union(edge[0], edge[1])
        last = edge[2]

result -= last

print(result)