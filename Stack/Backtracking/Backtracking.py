def powerset(n, k, cursum):
    if cursum == goal:
        for i in range(n):
            if A[i]:
                print(arr[i], end = " ")
        print()
        return
    elif cursum > goal:
        return
    else:
        if n == k:
            return
        A[k] = 1
        powerset(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset(n, k + 1, cursum)


# 이거 코드 이상함
def powerset2(n, k, cursum):
    if cursum > goal:
        return    
    if n == k:
        for i in range(n):
            if A[i]:
                print(arr[i], end = " ")
        print()
        return
    else:
        A[k] = 1
        powerset2(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset2(n, k+1, cursum)


arr = [i for i in range(1, 11)]
goal = 10
A = [0]*10
powerset2(10, 0, 0)
