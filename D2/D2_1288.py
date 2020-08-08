t = int(input())

def check(a):
    for num in a:
        if num == 0:
            return False
    return True

for i in range(t):
    n = int(input())
    num_list = [0 for _ in range(10)]
    cnt = n
    j = 1
    while True:        
        for k in range(10):
            if str(k) in str(cnt): num_list[k] += 1        
        if check(num_list):
            print('#'+str(i+1), n*j)
            break
        cnt += n
        j    += 1