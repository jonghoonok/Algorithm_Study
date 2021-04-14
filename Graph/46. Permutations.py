def permute_1(self, nums: List[int]) -> List[List[int]]:
    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])
            return
        
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    
    result = []
    prev_elements = []
    dfs(nums)
    return result


# 전통적인 자리바꾸기
def permute_2(nums):
    def perm(arr, depth, n):
        if depth == n:
            result.append(arr[:])
            return
        
        for idx in range(depth, n):
            arr[idx], arr[depth] = arr[depth], arr[idx]
            perm(arr, depth+1, n)
            arr[idx], arr[depth] = arr[depth], arr[idx]

    result = []
    perm(nums, 0, len(nums))
    return result

nums = [1,2,3]
print(permute_2(nums))