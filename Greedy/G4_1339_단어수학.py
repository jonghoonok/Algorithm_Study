n = int(input())
words = [[] for _ in range(8)]      # 각 자릿수별로 알파벳을 담을 리스트, 0번 인덱스에 1의 자리, 1번 인덱스에 10의자리 ...
alphabets = []                      # 사용된 모든 알파벳을 중복 없이 담는 리스트
for _ in range(n):
    word = input()
    for i in range(len(word)):
        words[i].append(word[-1-i])
        if word[i] not in alphabets: alphabets.append(word[i])

# 알파벳별로 중요도를 매겨서 숫자를 부여함
# 자릿수가 높은 알파벳이 중요도가 높음: words의 가장 마지막 인덱스에 등장하면 중요도 최상위
priority_list = [0]*len(alphabets)
temp = 1            # 자릿수에 따라 매길 중요도
for element in words:
    # 해당 자릿수의 알파벳에 대해 중요도를 더해 priority 리스트에 저장함
    for alphabet in element:
        i = alphabets.index(alphabet)
        priority_list[i] += temp
    temp *= 10      # 자릿수가 바뀌기 때문에 중요도에 10을 곱해줌

# 중요도가 높은 순으로 9에서부터 숫자를 매겨 다 더해주면 그것이 결과임
result = 0
priority_list.sort(reverse=True)
num = 9
for priority in priority_list:
    result += num * priority
    num -= 1
print(result)