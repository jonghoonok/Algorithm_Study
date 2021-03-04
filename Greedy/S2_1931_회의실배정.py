n = int(input())
arr = []
result = 0
meeting_room=[]

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(reverse=True)                      # 시작시간이 늦은 순서대로 정렬
meeting_room.append(arr[0])                 # 가장 늦게 시작하는 회의를 넣음
result += 1

for i in range(1, n):                       # arr[0]은 이미 넣었으니 skip
    if arr[i][1] <= meeting_room[-1][0]:    # 예약된 회의 중 가장 늦게 시작하는 것의 시작시각보다 종료시각이 같거나 빠르면 예약 
        meeting_room.append(arr[i])
        result += 1

print(result)