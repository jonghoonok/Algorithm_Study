def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    if not n:
        return None
    if n == 1:
        return nums[0]

    mid = n // 2
    a = self.majorityElement(nums[:mid])
    b = self.majorityElement(nums[mid:])

    return [b, a][nums.count(a) > mid]

# DP 
def majorityElement(self, nums: List[int]) -> int:
    cnt = collections.defaultdict(int)
    for num in nums:
        if cnt[num] == 0:
            # memoization: 한번 카운트를 계산한 값을 저장
            cnt[num] = nums.count(num)
        
        if cnt[num] > len(nums) // 2:
            return num