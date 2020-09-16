def big_num():
    if N == 1:
        return numList[0]
    else:
        cnt = 0
        temp = 0
        result = 0
        numList.sort()
        
        while cnt < M:
            result += numList[-1]
            cnt += 1
            temp += 1
            if temp == K and cnt < M-1:
                temp = 0
                result += numList[-2]
                cnt += 1
        
        return result

# 더 빠른 방법
def big_num2():
    if N == 1:
        return numList[0]
    else:        
        numList.sort()
        # 가장 큰 수와 그 다음 수가 K+1의 주기로 각각 K번, 1번씩 더해짐을 이용
        result = (M//(K+1))*numList[-2] + ((M//(K+1))*K + M%(K+1))*numList[-1]
        return result


N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
print(big_num())