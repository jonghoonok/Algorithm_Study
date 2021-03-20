table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preferences = [7, 5, 5]

    # 직업군 별로 언어 선호도 x 직업군 언어 점수의 총합을 저장하는 배열
    results = [0]*5

    new_table = [[] for _ in range(5)]
    for i in range(5):
        new_table[i] = list(table[i].split())

    # 각 직업군에 대해 계산
    for i in range(5):
        # 선호도 x 직업군 언어 점수의 총합
        score = 0   
        # 언어별로 선호도 x 직업군 언어 점수를 계산하여 score에 더함
        for j in range(1, 6):
            # language 배열을 돌며 해당 언어가 존재하면 선호도 점수를 읽어서 계산
            for k in range(len(languages)):
                if new_table[i][j] == languages[k]:
                    # 선호도preferences[k] * 직업군 언어 점수(6-j)
                    score += preferences[k] * (6-j)
                    break
                k += 1

        results[i] = score

    # results 테이블에서 가장 점수가 높은 직업군이 결과가 됨
    # 총합이 같은 직업군이 여러 개일 경우, 사전 순으로 가장 빠른 직업군을 return 하기 위해 results의 순서를 변경
    # CONTENTS, GAME, HW, PORTAL, SI순으로 변경
    new_result = [results[1],results[4],results[2],results[3],results[0]]

    result = 0
    index = 0
    for i in range(5):
        if new_result[i] > result:
            result = new_result[i]
            index = i

    ans = 0
    if index == 0:
        ans = 1
    elif index == 1:
        ans = 4
    elif index == 2:
        ans = 2
    elif index == 3:
        ans = 3
    else:
        ans = 0

    print(new_table[ans][0])