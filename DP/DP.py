# Top-Down
d = [0]*100
def pibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n]:
        return d[n]
    else:
        d[n] = pibo(n-1) + pibo(n-2)
        return d[n]

# Bottom-Up
def pibo2(n):
    d2 = [0]*100
    d2[1] = d2[2] = 1
    
    for i in range(3, 100):
        d2[i] = d2[i-1] + d2[i-2]
    
    return d2[n]

print(pibo(30))
print(pibo2(30))