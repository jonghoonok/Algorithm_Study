from itertools import combinations

# 단어를 2진수로 변환하기 위한 해시맵
# b~z 순으로: bdz = 0b101000000000000000001
bin_alpha = {
    'b':20,
    'd':19,
    'e':18,
    'f':17,
    'g':16,
    'h':15,
    'j':14,
    'k':13,
    'l':12,
    'm':11,
    'o':10,
    'p':9,
    'q':8,
    'r':7,
    's':6,
    'u':5,
    'v':4,
    'w':3,
    'x':2,
    'y':1,
    'z':0,
}


# 단어를 2진수로 변환
def word_to_bin(word):
    result = 0
    for letter in word:
        result += (1 << bin_alpha[letter])
    return result


n, k = map(int, input().split())
words = []
for _ in range(n):
    # 각 단어에서 a, n, t, i, c를 제외한 알파벳들의 집합을 저장
    words.append(set(input()[4:-4]).difference('a', 'n', 't', 'i', 'c'))

# 읽을 수 있는 단어가 없음: a, n, t, i, c도 가르칠 수 없는 경우
if k < 5:
    print(0)
else:
    bin_words = [word_to_bin(x) for x in words]

    # 2의 0제곱부터 20제곱까지 21개
    power_of_two = []
    for i in range(21):
        power_of_two.append(2 ** i)

    # 21Ck-5의 모든 조합에 대해 words에 있는 단어 중 가장 많이 가르칠 수 있는 조합을 구함
    result = 0
    for comb in combinations(power_of_two, k-5):
        temp = 0
        cur = sum(comb)
        for bin_word in bin_words:
            if cur & bin_word == bin_word:
                temp += 1
        if temp > result:
            result = temp
    
    print(result)