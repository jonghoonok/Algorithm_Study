# 내 풀이: DP인데 상당히 느림(7516ms)
def longestPalindrome_1(s: str) -> str:
    n = len(s)

    # store the lenth of palindrome which starts from index i to j
    lcs = [[False]*n for _ in range(n)]

    # length 1 palindrome
    for i in range(n):
        lcs[i][i] = True

    # length 2 palindrome
    for i in range(n-1):
        if s[i] == s[i+1]:
            lcs[i][i+1] = True

    # lenth n palindrome
    for i in range(3, n+1):
        for j in range(n-i+1):
            if lcs[j+1][j+i-2] and s[j] == s[j+i-1]:
                lcs[j][j+i-1] = True

    # find longest palindrome
    length = 0
    start, end = 0, 0
    for i in range(n):
        for j in range(i, n):
            if lcs[i][j] and (j-i+1 > length):
                length = j-i+1
                start, end = i, j
    
    return s[start:end+1]

# 풀이2: 투 포인터+슬라이딩 윈도우
def longestPalindrome_2(s: str) -> str:
        n = len(s)
        # 길이 1이거나 통채로 팰린드롬인 경우
        if n < 2 or s == s[::-1]:
            return s
        
        # 나머지 경우: 짝수 팰린드롬 or 홀수 팰린드롬
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < n and s[left]==s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        result = ''
        # 중첩 합수를 활용한 슬라이딩 윈도우의 이동
        for i in range(n-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        
        return result

s = "babad"
print(longestPalindrome_2(s))