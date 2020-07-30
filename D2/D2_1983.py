import sys

sys.stdin = open("D2_1983_input.txt", "r")

t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    gradeList = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    scoreList = []
    for j in range(n):
        mid, final, homework = map(int, input().split())
        scoreList.append(0.35*mid + 0.45*final + 0.2*homework)
    
    kScore = scoreList[k-1]
    scoreList.sort()
    scoreList.reverse()
    
    result = gradeList[scoreList.index(kScore)*10//n]

    print('#'+str(i+1), result)