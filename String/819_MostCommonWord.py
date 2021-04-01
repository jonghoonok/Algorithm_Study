# from collections import defaultdict

# 내 답안: 잘못됨
# 마지막에 문자로 끝나는 경우 한 글자가 짤림
def mostCommonWord(paragraph, banned) -> str:
    words = collentions.defaultdict(int)
    n = len(paragraph)
    i = 0
    while i < n:
        # pop a word
        for j in range(i, n):
            # 여기서 paragraph가 문자로 끝나면 j는 n-1인채로 끝나는데
            if not paragraph[j].isalpha():
                break

        # j 전까지만 입력하기 때문에 마지막 한 글자가 잘리게 됨...
        # 예외처리 해주니까 통과하긴 했다
        if paragraph[i:j] not in banned:
            words[paragraph[i:j].lower()] += 1
        
        # move to next word
        for k in range(j, n):
            if paragraph[k].isalpha():
                i = k
                break
        
        if k == n-1:
            break    
        
    cnt = 0
    ans = ''
    for key, value in words.items():
        if value > cnt:
            ans = key
            cnt = value
    
    return ans


# Counter 객체를 이용한 풀이
def mostCommonWord_2(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


# defaultdict를 이용한 풀이
def mostCommonWord_3(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)