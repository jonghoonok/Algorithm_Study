def pow(num, div):
    if div == 0:
        return 1
    elif div % 2 == 0:
        temp = pow(num, div//2) % c
        return (temp**2) % c
    else:
        temp = pow(num, div//2) % c
        return ((temp**2) % c * num) % c

a, b, c = map(int, input().split())
print(pow(a,b))