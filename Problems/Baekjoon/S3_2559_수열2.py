n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = sum(arr[:k])
temp = result
for i in range(k, n):
    temp += arr[i]
    temp -= arr[i-k]
    if temp > result:
        result = temp

print(result)