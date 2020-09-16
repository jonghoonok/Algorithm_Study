def powerset(n, k, cursum):
    global total
    # 가지치기: 현재의 합이 goal을 넘어가면 skip
    if cursum > goal:
        return    
    
    total += 1
    if cursum == goal:
        for i in range(n):
            if check[i]:
                print(arr[i], end = " ")
        print()
    else:
        if k == n:
           return
        else:
            check[k] = 1
            powerset(n, k+1, cursum+arr[k])
            check[k] = 0
            powerset(n, k+1, cursum)

n = 10
goal = 10
arr = [i for i in range(1, n+1)]
check = [0]*10
total = 0
powerset(n, 0, 0)
print("호출 횟수: {}회".format(total))