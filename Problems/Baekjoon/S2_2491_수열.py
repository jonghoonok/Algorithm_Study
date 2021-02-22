n = int(input())
nums = list(map(int, input().split()))

ascend = 1
decend = 1
temp = 1    # 현재 보고 있는 수열의 길이

# 가장 긴 증가하는 수열의 길이 찾기
for i in range(1, n):
    if nums[i] >= nums[i-1]:
        temp += 1
    else:
        if temp > ascend:
            ascend = temp 
        temp = 1
# 주의: 가장 긴 수열이 마지막에 있으면 반영되지 않으니 for문 종료 후에도 검사 필요
if temp > ascend:
    ascend = temp 
temp = 1

# 가장 긴 감소하는 수열의 길이 찾기
for i in range(1, n):
    if nums[i] <= nums[i-1]:
        temp += 1
    else:
        if temp > decend:
            decend = temp 
        temp = 1
if temp > decend:
    decend = temp 

result = ascend if ascend > decend else decend
print(result)