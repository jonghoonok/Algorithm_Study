import sys

sys.stdin = open("D2_4866_input.txt", "r")


def parentheses_check(words):
    left = ['{', '(']
    right = ['}', ')']
    stack = []
    for letter in words:
        if letter in left:
            stack.append(letter)
        elif letter in right:
            if not stack:
                return 0
            if right.index(letter) != left.index(stack.pop()):
                return 0
    if stack:
        return 0
    else:
        return 1


t = int(input())
for test in range(t):
    words = input()    
    print('#'+str(test+1), parentheses_check(words))