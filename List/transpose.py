# N, M = map(int, input().split())
# arr = [list(map(intm input.split())) for _ in range(N)]

# 전치행렬 코드
for i in range(N):
    for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]            


# 한 리스트에서 뽑을 수 있는 숫자쌍
arr = [1, 2, 3, 4]

for i in range(len(arr) - 1):
    for j in range(i+1, len(arr)):
        print((arr[i], arr[j]), end = " ")