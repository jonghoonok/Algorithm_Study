def isValid(s: str) -> bool:

    stack = []
    pair = {'(': ')', '{': '}', '[': ']'}
    for p in s:
        if p in pair:
            stack.append(p)
        elif not stack or pair[stack.pop()] != p:
            return False

    return len(stack) == 0

s = "([)]"
print(isValid(s))