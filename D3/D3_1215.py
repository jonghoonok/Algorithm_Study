import sys

sys.stdin = open("D3_1215_input.txt", "r")

def palindrome():
    cnt = 0
    # 행 검색
    for i in range(8):
        for j in range(8-n+1):
            for k in range(n//2):
                if char_list[i][j] == char_list[i][j]

    # 열 검색

    return cnt

for test_case in range(1, 11):
    n = int(input())
    char_list = list(input().split())

    print('#' + str(test_case), palindrome())
