import sys


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# 인덱스를 편하게 다루기 위해 앞에 0 추가
nums.insert(0, 0)

# 미리 모든 경우의 수에 대해 팰린드롬을 이루는지 계산해 두고 s, e에 대해 출력
dp = [[0]*(n+1) for _ in range(n+1)]
# 먼저 길이1 팰린드롬과 길이2 팰린드롬(연속한 두 수가 같다면)에 대해 dp에 True를 기록
for i in range(1, n+1):
    dp[i][i] = 1
    if nums[i-1] == nums[i]:
        dp[i-1][i] = 1

# 길이 3부터 n까지의 팰린드롬을 기록
for i in range(3, n+1):
    for j in range(1, n-i+2):
        # 시작과 끝이 같고 그 내부가 팰린드롬을 이룬다면 팰린드롬
        if nums[j] == nums[j+i-1] and dp[j+1][j+i-2]:
            dp[j][j+i-1] = 1

m = int(sys.stdin.readline())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s][e])