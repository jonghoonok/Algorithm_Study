paper = [[0]*100 for _ in range(100)]
for _ in range(4):
    x, y, p, q = map(int, input().split())
    for i in range(x, p):
        for j in range(y, q):
            paper[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            result += 1

print(result)