import sys

sys.stdin = open("D2_1859_input.txt", "r")

t = int(input())

def sell(priceList):
    result = 0
    if len(priceList) == 1:
        return 0
    sellDay = priceList.index(max(priceList))
    if sellDay != 0:
        for i in range(sellDay):
            result += priceList[sellDay] - priceList[i]    
    if sellDay == len(priceList) - 1:
        return result
    return result + sell(priceList[sellDay+1:])

for test_case in range(t):
    n = int(input())    
    priceList = list(map(int, input().split()))        
    print('#'+str(test_case+1), sell(priceList))    