import sys

def prefix_sum():
    for i in range(1, n+1):
        # i행과 i열을 채움
        for j in range(1, n+1):
            # 주의 : sum_arr의 i행은 arr의 i-1행에 해당
            sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]
            sum_arr[j][i] = sum_arr[j-1][i] + sum_arr[j][i-1] - sum_arr[j-1][i-1] + arr[j-1][i-1]


n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

# 구간합을 미리 저장해 둠
sum_arr = [[0]*(n+1) for _ in range(n+1)]
prefix_sum()

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum_arr[x2][y2]-sum_arr[x2][y1-1]-sum_arr[x1-1][y2]+sum_arr[x1-1][y1-1])