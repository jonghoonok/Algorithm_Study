# 반복
def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n-1
    mid = n // 2
    while l <= r:
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
        mid = (l + r) // 2

    return -1

# 재귀 
def search(self, nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if target < nums[mid]:
            return binary_search(left, mid-1)
        elif target > nums[mid]:
            return binary_search(mid+1, right)
        else:
            return mid
    
    return binary_search(0, len(nums)-1)


# bisect 모듈
def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    return index if index < len(nums) and nums[index] == target else -1
