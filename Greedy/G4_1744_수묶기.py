import sys


def bind(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        result = 0
        length = len(arr)
        for i in range(0, length - 1, 2):
            # 둘 중 하나가 1이면 곱하지 않고 더하는 것이 낫다
            if arr[i] == 1 or arr[i+1] == 1:
                result += arr[i] + arr[i+1]
            else:
                result += arr[i]*arr[i+1]
        
        if length % 2 == 1:
            result += arr[-1]
        
        return result


n = int(input())
plus = []
minus = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()            # 음수는 작은 수일수록 절대값이 크다는 것이 포인트

print(bind(plus) + bind(minus))