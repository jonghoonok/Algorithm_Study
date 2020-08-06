import sys

sys.stdin = open("D3_1216_input.txt", "r")


def palindrome(words):
    result = 0
    for i in range(1, 101):
        for j in range(101 - i):
            if list(words[j:i+j]) == list(reversed(words[j:i+j])):
                if result < i:
                    result = i
    return result


def palindrome2(matrix):
    result = 0

    # 행 검색
    for i in range(100):
        if palindrome(matrix[i]) > result:
            result = palindrome(matrix[i])

    # 열 검색
    for i in range(100):
        column = ''
        for j in range(100):
            column += matrix[j][i]
        if palindrome(column) > result:
            result = palindrome(column)

    return result


for test_case in range(1, 11):
    n = int(input())
    char_list = [input() for _ in range(100)]
    print('#' + str(test_case), palindrome2(char_list))
