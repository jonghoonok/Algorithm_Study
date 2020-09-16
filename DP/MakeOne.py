def make_one(n):
    d = [0]*30001    

    for i in range(2, n+1):
        
        d[i] = d[i-1] + 1
        
        if i % 2 == 0:
            d[i] = min(d[i//2], d[i-1]) + 1
        if i % 3 == 0:
            d[i] = min(d[i//3], d[i-1]) + 1
        if i % 5 == 0:
            d[i] = min(d[i//5], d[i-1]) + 1           

    return d[n]


print(make_one(26))