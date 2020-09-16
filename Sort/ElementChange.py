N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
i = 0
while K:
    if A[i] < B[-i]:
        A[i], B[-i] = B[-i], A[i]
    else:
        break
    K -= 1

print(sum(A))
