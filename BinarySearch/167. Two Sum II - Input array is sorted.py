# 이진 탐색
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def binary_search2(arr, start, end, target):
        while start <= end:
            mid = (start + end)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return None

    n = len(numbers)
    for i in range(n):
        index = binary_search(numbers, i+1, n-1, target-numbers[i])
        if not index:
            return [i+1, index+1]


# 투 포인터
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]