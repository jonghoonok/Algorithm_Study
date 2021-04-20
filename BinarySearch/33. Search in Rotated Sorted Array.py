# O(n)
def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    # pivot 찾기
    pivot = 0
    for i in range(n-1):
        if nums[i+1] < num[i]:
            pivot = i+1
            break
    # target 찾기
    new_nums = nums[pivot:] + nums[:pivot]
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if target < new_nums[mid]:
            r = mid-1
        elif target > new_nums[mid]:
            l = mid+1
        else:
            # 변환하여 리턴
            return mid - n + pivot if mid >= n - pivot else mid + pivot
    
    return -1


# O(logn)
def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    # pivot찾기는 사실 이진탐색으로 가능함
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid + 1
    pivot = r

    # pivot기준 이진 탐색
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        mid_pivot = (mid+pivot) % n
        if target < nums[mid_pivot]:
            r = mid - 1
        elif target > nums[mid_pivot]:
            l = mid + 1
        else:
            return mid_pivot
    return -1