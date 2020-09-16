def to_one():
    global N
    cnt = 0    
    while N > 1:
        if N % K == 0:
            N /= K
        else:
            N -= 1
        cnt += 1
    return cnt

# 좀 더 빠른 방법
def to_one2():
    global N
    cnt = 0    
    while N > 1:
        target = (N // K) * K
        cnt += N - target
        N = target // K
    return cnt

N, K = map(int, input().split())
print(to_one())