n = int(input())
nums = list(map(int, input().split()))
DP = [0]*n
DP[0] = nums[0]
for i in range(1, n):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i] and temp < DP[j]:
            temp = DP[j]
    DP[i] = temp + nums[i]

print(max(DP))