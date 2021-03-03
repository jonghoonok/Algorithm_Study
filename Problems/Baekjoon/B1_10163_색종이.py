n = int(input())
arr = [[0]*101 for _ in range(101)]
for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            arr[j][k] = i

result = [0]*n
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            result[arr[i][j]-1] += 1

for i in range(n):
    print(result[i])