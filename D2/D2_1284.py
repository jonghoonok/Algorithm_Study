t = int(input())
for i in range(t):
    p, q, r, s, w = map(int, input().split())
    
    a = p*w
    b = q + (w-r)*s if w> r else q
    
    if a>b:
        print('#'+str(i+1), b)
    else:
        print('#'+str(i+1), a)