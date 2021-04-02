# 내가 푼거지만 오졌다... (28ms)
# 딕셔너리에 저장하는 동시에 탐색하기 때문에 4에 비해 시간이 거의 절반임
def twoSum_1(nums, target):
        check = dict()
        for i in range(len(nums)):
            if check.get(target - nums[i]) is not None:
                return [i, check.get(target - nums[i])]
            else:
                check[nums[i]] = i


# BruteForce...
def twoSum_2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum_3(nums, target):
    for i, n in enumerate(nums):
        compliment = target - n
        if compliment in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(compliment)+(i+1)]


# dict를 이용했는데 내것보다 느림: 저장하고 나서 탐색하기 때문
def twoSum_4(nums, target):
    nums_map = dict()
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 내것과 거의 비슷한데도 느림: enumerate가 느린듯
def twoSum_5(nums, target):
    nums_map = dict()
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투 포인터 이용
def twoSum_5(nums, target):
    pass

nums = [3,2,4]
target = 6
print(twoSum(nums, target))