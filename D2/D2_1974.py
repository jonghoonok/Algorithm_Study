import sys

sys.stdin = open("D2_1974_input.txt", "r")


def check(matrix):    
    # 가로 방향 체크
    for i in range(9):
        checkList = [0 for _ in range(9)]
        for j in range(9):
            checkList[matrix[i][j]-1] += 1            
        if 0 in checkList: return 0
   
    # 세로 방향 체크
    for i in range(9):
        checkList = [0 for _ in range(9)]
        for j in range(9):
            checkList[matrix[j][i]-1] += 1            
        if 0 in checkList: return 0
   
    # 격자 내부 체크
    for i in range(9):
        checkList = [0 for _ in range(9)]
        for j in range(9):
            checkList[matrix[3*(i//3) + j//3][j%3]-1] += 1            
        if 0 in checkList: return 0
    
    
    # 3번 체크해서 맞으면 1을 리턴
    return 1

t = int(input())
for test in range(t):
    sudoku = [list(map(int, input().split())) for _ in range(9)]    
    print('#'+str(test+1), check(sudoku))