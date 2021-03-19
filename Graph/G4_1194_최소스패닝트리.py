import sys


def find_root(x):
    if root[x-1] != x:
        root[x-1] = find_root(root[x-1])
    return root[x-1]


def union(x, y):
    x = find_root(x)
    y = find_root(y)
    if x < y:
        root[y-1] = x
    else:
        root[x-1] = y


V, E = map(int, input().split())
edges = [[0]*3 for _ in range(E)]
for i in range(E):
    a, b, c = map(int, input().split())
    edges[i][0], edges[i][1], edges[i][2] = a, b, c

edges.sort(key=lambda x:x[2])

root = [i+1 for i in range(V)]

cnt = 0
total_cost = 0
for edge in edges:
    rx = find_root(edge[0])
    ry = find_root(edge[1])

    if rx == ry:
        continue
    else:
        cnt += 1
        union(rx, ry)
        total_cost += edge[2]

    if cnt == V-1:
        break

print(total_cost)