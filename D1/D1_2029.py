n = int(input())

for i in range(n):
    a, b = map(int, input().split(" "))
    div = a//b
    mod = a%b
    print('#'+str(i+1), div, mod)