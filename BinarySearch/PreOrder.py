n = int(input())

Tree = [[0]*4 for _ in range(n+1)]
for i in range(1,n+1):
    Tree[i][0] = i

edges = list(map(int, input().split()))
for i in range(0, (n-1)*2, 2):
    a, b = edges[i], edges[i+1]

    if not Tree[a][1]:
        Tree[a][1] = b
    else:
        Tree[a][2] = b
    Tree[b][3] = a

def preorder(node):
    if node:
        print(node, end=" ")
        preorder(Tree[node][1])
        preorder(Tree[node][2])

preorder(1)