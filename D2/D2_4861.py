import sys

sys.stdin = open("D2_4861_input.txt", "r")


def palindrome(letters):    
    # 가로 체크
    for x in range(n):
        for y in range(n-m+1):
            for i in range(m//2):
                if letters[x][y+i] != letters[x][y+m-1-i]:
                    break                
                if i == m//2 -1:
                    return letters[x][y:y+m]

    # 세로 체크
    for x in range(n-m+1):
        for y in range(n):
            for i in range(m//2):
                if letters[x+i][y] != letters[x+m-1-i][y]:
                    break
                if i == m//2 -1:
                    result = ''
                    for j in range(m):
                        result += letters[x+j][y]
                    return result


t = int(input())
for test in range(t):
    n, m = map(int, input().split())
    letters = [input() for _ in range(n)]
    print('#'+str(test+1), palindrome(letters))
