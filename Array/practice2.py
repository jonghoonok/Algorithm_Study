def powersum(arr):
    
    cnt = 0
    for i in range(1, 1<<len(arr)):
        powersum = 0
        for j in range(len(arr)):
            if i & 1<<j:
                powersum += arr[j]
        if powersum == 0: cnt +=1
    return cnt

arr = [-3, 3, -9, 6, 7 ,-6, 1, 5, 4, -2]

print(powersum(arr))