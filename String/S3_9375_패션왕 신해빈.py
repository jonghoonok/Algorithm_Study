from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    
    clothes = defaultdict(int)
    # 의상 종류별로 의상 하나씩 추가하기
    for _ in range(n):
        cloth, cloth_type = input().split(' ')
        clothes[cloth_type] += 1

    # 전체 조합의 수는 의상 종류별 의상의 수를 모두 곱하고 1을 빼면(아무것도 안 입은 상태) 됨
    result = 1
    for k, v in clothes.items():
        result *= v+1

    print(result-1)