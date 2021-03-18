n = int(input())
for _ in range(n):
    ps = list(input())
    stack = []
    flag = True
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                flag = False
                break
            stack.pop()
    if stack or not flag:
        print('NO')
    else:
        print('YES')