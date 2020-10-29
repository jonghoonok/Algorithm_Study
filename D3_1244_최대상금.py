import sys

sys.stdin = open("D3_1244_최대상금_input.txt", "r")


def max_prize(arr, n, cnt):
    if cnt == m:
        # 내장함수를 쓰지않고 정수로 바꾸려했는데 어째선지 더 오래걸려 주석처리함
        # result = 0
        # for i in range(n):
        #     result += arr[i]*(10**(n-1-i))
        # return result
        return int(''.join(arr))
    else:
        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                arr[i], arr[j] = arr[j], arr[i]
                # memoization 
                # 이미 해당 교환 횟수에 대해 같은 수를 만든 적 있다면 skip
                if ''.join(arr) in table[cnt]:
                    arr[i], arr[j] = arr[j], arr[i]
                    continue
                else:
                    table[cnt].append(''.join(arr))
                    temp = max_prize(arr, n, cnt+1)
                    arr[i], arr[j] = arr[j], arr[i]
                if temp > result:
                    result = temp
        return result
    

t = int(input())
for test_case in range(t):
    n, m = input().split()
    # n = [int(num) for num in n]
    n = list(n)
    m = int(m)
    
    # memoization을 위한 테이블
    table = [[] for _ in range(m)]
    print('#' + str(test_case + 1), max_prize(n, len(n), 0))