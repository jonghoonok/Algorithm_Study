import sys

sys.stdin = open("D2_2005_input.txt", "r")

t = int(input())

def pascal(n):
    pascalList = []
    for i in range(n):
        pascalList_i = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp = 1
                pascalList_i.append(temp)
            else:              
                temp = pascalList[i-1][j-1] + pascalList[i-1][j]
                pascalList_i.append(temp)
            print(temp, end=' ')
        pascalList.append(pascalList_i)
        print()

for test_case in range(t):
    n = int(input())    
    print('#'+str(test_case+1))
    pascal(n)