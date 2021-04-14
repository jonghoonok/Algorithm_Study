def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(elements, index, cursum):
        if cursum >= target:
            if cursum == target:
                results.append(elements)
            return

        for i in range(index, n):
            dfs(elements + [candidates[i]], i, cursum + candidates[i])

    results = []
    n = len(candidates)
    dfs([], 0)
    return results