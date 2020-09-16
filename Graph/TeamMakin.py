def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def check(x, y):
    if find_parent(x) == find_parent(y):
        return 'YES'
    else:
        return 'NO'


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        union(a, b)
    else:
        print(check(a, b))
