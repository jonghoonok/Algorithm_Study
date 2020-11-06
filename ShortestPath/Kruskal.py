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
def make_set(x):
    P[x] = x


def find_set(x):
    if P[x] == x:
        return x
    else:
        return find_set(P[x])


def union(x, y):
    P[find_set(y)] = find_set(x)


def mst():
    cnt = 0
    total = 0

    for i in range(E):
        px = find_set(edge[i][0])
        py = find_set(edge[i][1])

        # cycle check
        if px != py:
            total += edge[i][2]
            cnt += 1
            # union(edge[i][0], edge[i][1])
            P[py] = px
        if cnt == V-1:
            break
    return total


# 입력
V, E = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(E)]
edge.sort(key=lambda x: x[2])

# dis-joint
P = [0] * V

for i in range(V):
    make_set(i)

print(mst())