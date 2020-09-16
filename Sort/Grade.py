N = int(input())
grade_list = [input().split() for _ in range(N)]

# 람다함수의 인자는 뭐 x라고 하든 y라고 하든 상관없음
grade_list.sort(key=lambda x:x[1])

for student in grade_list:
    print(student[0], end=" ")