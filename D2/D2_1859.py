import sys

sys.stdin = open("D2_1859_input.txt", "r")


# 뒤에서부터 최댓값을 가지는 인덱스를 모아서 반환
def backward_max(numbers):
    temp_result = []
    result = [0]
    temp = 0
    for i in range(1, len(numbers)):
        if numbers[-i] >= temp:
            temp = numbers[-i]
            temp_result.append(len(numbers) - i)
    for i in range(1, len(temp_result)+1):
        result.append(temp_result[-i])
    return result


def sell(priceList):
    result = 0
    if len(priceList) == 1:
        return 0
    sell_day_list = backward_max(priceList)
    for i in range(1, len(sell_day_list)):
        if i == 1:
            for j in range(sell_day_list[i]):
                result += priceList[sell_day_list[i]] - priceList[j]
        else:
            # 여기서부터는 범위를 +1로 해줘야 함: 그렇지 않으면 이전의 최대가격을 빼버리게 됨
            for j in range(sell_day_list[i-1]+1, sell_day_list[i]):
                result += priceList[sell_day_list[i]] - priceList[j]

    return result


t = int(input())
for test_case in range(t):
    n = int(input())    
    priceList = list(map(int, input().split()))        
    print('#'+str(test_case+1), sell(priceList))
