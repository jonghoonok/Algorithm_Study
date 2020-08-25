import sys

sys.stdin = open("D3_1229_input.txt", "r")


def crypto_fix2(origin_numbers, order_numbers):
    cnt = 0
    while cnt < len(order_numbers):                        
        index = int(order_numbers[cnt+1])
        amount = int(order_numbers[cnt+2])
        if order_numbers[cnt] == 'I':
            insert_numbers = list(map(int, order_numbers[cnt+3:cnt+3+amount]))        
            for i in range(amount):
                origin_numbers.insert(index+i, insert_numbers[i])
            cnt += amount+3                   
        else:
            for i in range(amount):
                origin_numbers.pop(index)
            cnt += 3
        
    print(*origin_numbers[:10])


for test_case in range(10):
    n = int(input())    
    origin_numbers = list(map(int, input().split()))
    m = int(input())
    order_numbers = list(input().split())
    print('#' + str(test_case + 1), end=' ')
    crypto_fix2(origin_numbers, order_numbers)
