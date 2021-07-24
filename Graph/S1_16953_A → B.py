from collections import deque

def n_to_m():
    result = -1
    q = deque([(n, 1)])

    while q:
        t = q.popleft()
        
        if t[0] == m:
            result = t[1]
            break

        if t[0]*2 <= m:
            q.append((t[0]*2, t[1]+1))
        if t[0]*10+1 <= m:
            q.append((t[0]*10+1, t[1]+1))

    return result


n, m = map(int, input().split())
print(n_to_m())