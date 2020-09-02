import sys

sys.stdin = open("D2_4871_input.txt", "r")


def path(G, Start, Goal):
    visit = []
    stack = []
    stack.append(Start)
    while stack:
        w = stack.pop()
        if w == Goal:
            return 1
        if w not in visit:
            visit.append(w)
            stack.extend(G[w])
    return 0

visit = []
def path_recursive(G, Start, Goal):
    visit.append(Start)
    if Start == Goal:
        return 1
    for w in G[Start]:
        if w not in visit:
            if path_recursive(G, w, Goal):
                return 1
    return 0

t = int(input())
for test in range(t):
    V, E = map(int, input().split())
    
    # dict로 그래프 작성
    G = {i:[] for i in range(1, V+1)}
    for _ in range(E):
        v, e = map(int, input().split())
        nodes = G[v]
        nodes.append(e)
    Start, Goal = map(int, input().split())
    # print(G)
    
    print('#'+str(test+1), path(G, Start, Goal))