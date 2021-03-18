import sys

def zero_python():
    for i in range(n):
        num = int(sys.stdin.readline())
        if num:
            nums.append(num)
        else:
            nums.pop()

    print(sum(nums))


# 풀이2: append와 pop은 오래걸리니 C 스타일 stack을 활용해보자
def zero_C():
    ptr = 0
    stack = [0]*n
    for i in range(n):
        num = int(sys.stdin.readline())
        if num:
            stack[ptr] = num
            ptr += 1
        else:
            ptr -= 1
            stack[ptr] = 0
        
    print(sum(stack))


n = int(input())
nums = []
# zero_python()
zero_C()