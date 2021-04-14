# 내 풀이
def letterCombinations_1(digits: str):
    def dfs(nums, word):
        if not nums:
            result.append(word)
            return
        for char in graph[nums[0]]:
            dfs(nums[1:], word+char) 

    result = []     
    dfs(digits, "")
    return result

    graph = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }


# 책의 풀이
def letterCombinations_2(digits: str):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1, path+j)

    # 예외 처리
    if not digits:
        return []

    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []
    dfs(0, "")
    return result

print(letterCombinations_2("23"))    