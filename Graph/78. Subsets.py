# 풀이1: 비트마스크
def subsets_1(nums):
    results = []
    n = len(nums)
    
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if 1<<j & i:
                temp.append(nums[j])
        results.append(temp)
    
    return results


# DFS
def subsets_2(nums):
        results = []
        n = len(nums)

        def dfs(index, arr):
            if index == n:
                results.append(arr[:])
                return
            
            dfs(index+1, arr)
            dfs(index+1, arr+[nums[index]])
        
        dfs(0, [])
        return results


nums = [1,2,3]
print(subsets_2(nums))