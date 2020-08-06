import sys

sys.stdin = open("D3_1215_input.txt", "r")

def palindrome():
    cnt = 0
    # 행 검색
    for i in range(8):
        for j in range(8-n+1):
            check = 0
            for k in range(n//2):
                if char_list[i][j+k] == char_list[i][j+n-k-1]:
                    check += 1
                else:
                    break
            if check == n//2:
                cnt += 1
    # 열 검색
    for i in range(8):
        for j in range(8-n+1):
            check = 0
            for k in range(n//2):
                if char_list[j+k][i] == char_list[j+n-k-1][i]:
                    check += 1
                else:
                    break
            if check == n//2:
                cnt += 1

    return cnt

for test_case in range(1, 11):
    n = int(input())
    char_list = [list(input()) for _ in range(8)]

    print('#' + str(test_case), palindrome())
