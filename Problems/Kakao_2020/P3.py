def solution(info, query):
    answer = []
    
    info_dict = {
        'lang':{
            'cpp':[],
            'java':[],
            'python':[]
        },
        'pos':{
            'backend':[],
            'frontend':[]
        },
        'lev':{
            'junior':[],
            'senior':[],
        },
        'food':{
            'chicken':[],
            'pizza':[]
        },
        'score':{}
    }
    # info dict에 지원자 정보를 입력
    for i in range(len(info)):
        data = list(info[i].split())        
        for j in range(5):            
            if j == 0:
                if data[j] == 'cpp':
                    info_dict['lang']['cpp'].append(i)
                elif data[j] == 'java':
                    info_dict['lang']['java'].append(i)
                elif data[j] == 'python':
                    info_dict['lang']['python'].append(i)                    
            elif j == 1:
                if data[j] == 'backend':
                    info_dict['pos']['backend'].append(i)
                elif data[j] == 'frontend':
                    info_dict['pos']['frontend'].append(i)
            elif j == 2:
                if data[j] == 'junior':
                    info_dict['lev']['junior'].append(i)
                elif data[j] == 'senior':
                    info_dict['lev']['senior'].append(i)
            elif j == 3:
                if data[j] == 'chicken':
                    info_dict['food']['chicken'].append(i)
                elif data[j] == 'pizza':
                    info_dict['food']['pizza'].append(i)
            else:
                info_dict['score'][i] = int(data[j])


    # 쿼리를 읽어 answer 작성
    for q in query:
        # 각각의 쿼리 내용을 쪼개어 저장하는 리스트
        # 이거 시간 남으면 split안 쓰고 하나씩 읽으면서 검사하는걸로 변경 ㄱ
        q_list = list(q.split())
        # 쿼리를 읽어 연산
        temp = []
        for i in range(8):
            if q_list[i] == 'and':
                continue
            if q_list[i] == '-':                
                continue
            if i == 0:
                temp = info_dict['lang'][q_list[i]]
            elif i == 2:
                if not temp:
                    temp = info_dict['pos'][q_list[i]]
                else:
                    temp_temp = []
                    for j in range(len(temp)):
                        if temp[j] in info_dict['pos'][q_list[i]]:
                            temp_temp.append(temp[j])
                    temp = temp_temp
            elif i == 4:
                if not temp:
                    temp = info_dict['lev'][q_list[i]]
                else:
                    temp_temp = []
                    for j in range(len(temp)):
                        if temp[j] in info_dict['lev'][q_list[i]]:
                            temp_temp.append(temp[j])
                    temp = temp_temp
            elif i == 6:
                if not temp:
                    temp = info_dict['food'][q_list[i]]
                else:
                    temp_temp = []
                    for j in range(len(temp)):
                        if temp[j] in info_dict['food'][q_list[i]]:
                            temp_temp.append(temp[j])
                    temp = temp_temp
            else:
                cnt = 0
                if not temp:
                    temp = [i for i in range(len(info))]
                for j in range(len(temp)):
                    if info_dict['score'][temp[j]] >= int(q_list[i]):
                        cnt += 1
                answer.append(cnt)
                
    return answer


a = list(input().split(','))
b = list(input().split(','))
print(solution(a, b))