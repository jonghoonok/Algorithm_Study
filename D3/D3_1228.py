import sys

sys.stdin = open("D3_1228_input.txt", "r")


def crypto_fix(origin_numbers, order_numbers):
    cnt = 1
    while cnt < len(order_numbers):                
        x = int(order_numbers[cnt])
        y = int(order_numbers[cnt+1])
        insert_numbers = list(map(int, order_numbers[cnt+2:cnt+2+y]))        
        for i in range(y):
            origin_numbers.insert(x+i, insert_numbers[i])
        cnt += y+3         
        
    print(*origin_numbers[:10])


for test_case in range(10):
    n = int(input())    
    origin_numbers = list(map(int, input().split()))
    m = int(input())
    order_numbers = list(input().split())
    print('#' + str(test_case + 1), end=' ')
    crypto_fix(origin_numbers, order_numbers)
