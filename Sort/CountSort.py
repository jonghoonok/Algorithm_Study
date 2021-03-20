arr = [3,5,6,8,1,8,3,5,9,0,1,3,5,3]

# 데이터의 최대 범위만큼의 길이를 갖는 배열 선언
count = [0]*n

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')