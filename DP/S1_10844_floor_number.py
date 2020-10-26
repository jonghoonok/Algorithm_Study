n = int(input())

# i행 j열에는 j라는 숫자로 끝나는 길이 i인 계단수의 갯수
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
dp = [[0]*10 for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = 0
for i in range(10):
    result += dp[n-1][i]

print(result%1000000000)