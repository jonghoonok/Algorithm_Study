import sys

sys.stdin = open("D3_1216_input.txt", "r")


# 하나의 문자열을 받아 그 안에 있는 회문의 최대 길이를 리턴
def find_palindrome(words):
    result = 0
    # 최대 길이에서부터 하나씩 줄이는 것이 더 빠름
    for i in range(100, 0, -1):
        for j in range(101 - i):
            if list(words[j:i+j]) == list(reversed(words[j:i+j])):    
                result = i
                return result


# 행렬을 받아 행과 열에 대해 각각 palindrome() 실시
def palindrome(matrix):
    result = 0

    # 행 검색
    for i in range(100):
        row = find_palindrome(matrix[i])
        if row > result:
            result = row

    # 열 검색
    for i in range(100):
        column = ''
        for j in range(100):
            column += matrix[j][i]
        col = find_palindrome(column)
        if col > result:
            result = col

    return result


for test_case in range(1, 11):
    n = int(input())
    char_list = [input() for _ in range(100)]
    print('#' + str(test_case), palindrome(char_list))
