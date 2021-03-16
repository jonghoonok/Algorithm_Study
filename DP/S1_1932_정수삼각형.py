import sys
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

score = [[0]*(i+1) for i in range(n)]
score[0] = tri[0]
for i in range(1, n):
    score[i][0] = score[i-1][0] + tri[i][0]
    for j in range(1, i):
        score[i][j] = max(score[i-1][j-1], score[i-1][j]) + tri[i][j]
    score[i][i] = score[i-1][i-1] + tri[i][i]

print(max(score[n-1]))