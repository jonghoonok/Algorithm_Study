def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def binary_search(arr, target):
        n = len(arr)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if target < arr[mid]:
                r = mid-1
            elif target > arr[mid]:
                l = mid+1
            else:
                return True
        return False
    
    result = []
    for num in nums1:
        if binary_search(nums2, num) and not binary_search(result, num):
            result.append(num)
    
    return result


# 투 포인터 
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while p1 < n1 and p2 < n2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                result.add(nums1[p1])
                p1 += 1
                p2 += 1
        
        return result