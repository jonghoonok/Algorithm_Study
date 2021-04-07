def dfs(i, now):
    global minVal, maxVal, add, sub, mul, div

    if i == n:
        minVal = min(minVal, now)
        maxVal = max(maxVal, now)
    else:
        if add:
            add -= 1
            dfs(i+1, now+nums[i])
            add += 1
        if sub:
            sub -= 1
            dfs(i+1, now-nums[i])
            sub += 1
        if mul:
            mul -= 1
            dfs(i+1, now*nums[i])
            mul += 1
        if div:
            div -= 1
            dfs(i+1, int(now/nums[i]))
            div += 1
    

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxVal = int(1e9)*(-1)
minVal = int(1e9)

dfs(1, nums[0])

print(maxVal)
print(minVal)