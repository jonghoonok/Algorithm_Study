# 풀이1: pythonic하게 slicing을 이용하여 밀어내기
def change_queue():
    for i in range(n):
        num = numbers[i]
        students[i+1 - num:i+1] = students[i - num:i]
        students[i - num] = i+1

    print(' '.join(map(str, students)))


# 풀이2: 반복문 이용하여 밀어내기인데 slicing하고 큰 차이는 없으니 생략


n = int(input())
numbers = list(map(int, input().split()))
students = [i+1 for i in range(n)]
change_queue()