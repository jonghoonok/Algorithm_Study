n, k = map(int, input().split())
students = [[0, 0] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    students[y-1][s] += 1

result = 0
for i in range(6):
    for j in range(2):
        temp = students[i][j] // k
        temp2 = students[i][j] % k
        result += temp
        if temp2:
            result += 1

print(result)