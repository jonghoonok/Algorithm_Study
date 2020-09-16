from itertools import combinations 

def solution(orders, course):
    course_cnt = {}
    
    for num in course:        
        for order in orders:
            if len(order) < num:
                continue        
            # 일단 str로 해보고 안되면 order를 리스트로 변환하자            
            order_sorted = sorted(list(order))
            coms = combinations(order_sorted, num)
            for com in coms:
                if not course_cnt.get(com):
                    course_cnt[com] = 1
                else:
                    course_cnt[com] += 1

    answer = []

    keys = list(course_cnt.keys())
    key_list = [[] for _ in range(course[-1]+1)]
    for key in keys:
        key_list[len(key)].append(key)
    
    for num in course:
        choice = []
        for key in key_list[num]:            
            if course_cnt[key] == 1:
                continue
            else:
                choice.append([course_cnt[key], key])
        if choice:
            choice.sort()
            max_cnt = choice[-1][0]
            for i in range(len(choice)-1, -1, -1):
                if choice[i][0] == max_cnt:
                    answer.append(''.join(choice[i][1]))
                else:
                    break
    
    answer.sort()
    

    print(answer)



orders = list(input().split())
course = list(map(int, input().split()))
solution(orders, course)