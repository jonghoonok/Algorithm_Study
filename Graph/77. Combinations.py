# 순열을 살짝 변형해 봄
def combine_1(n: int, k: int):
    def dfs(elements):
        if len(prev_elements) == k:
            result.append(prev_elements[:])
            return
        
        for i in range(len(elements)):
            next_elements = elements[i+1:]
            prev_elements.append(elements[i])
            dfs(next_elements)
            prev_elements.pop()

    result = []
    prev_elements = []
    dfs(range(1, n+1))
    return result


# 책의 풀이
def combine_2(n: int, k: int):
    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    results = []
    dfs([], 1, k)
    return results

print(combine(4, 2))