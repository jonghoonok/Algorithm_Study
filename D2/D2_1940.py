import sys

sys.stdin = open("D2_1940_input.txt", "r")

t = int(input())

for test_case in range(t):
    n = int(input())
    v = 0
    s = 0
    for j in range(n):
        try:
            com, acc = map(int, input().split())        
            if com == 1:          
                v += acc                            
            elif com == 2:            
                v -= acc
                if v < 0: v = 0
            s += abs(v)
        except:            
            s += abs(v)
    print('#'+str(test_case+1), s)