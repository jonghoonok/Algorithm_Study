from collections import deque

# 문자열을 직접 양쪽에서부터 탐색하며 판별: 100ms
def is_palindrome_1(s):
    n = len(s)
    i = 0
    j = n-1
    ascii = list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))
    while i <= j:
        # 공백을 건너뜀
        while ord(s[i]) not in ascii:
            i += 1
        while ord(s[j]) not in ascii:
            j -= 1

        # 만약 교차가 일어났으면 break
        if i >= j:
            break

        # 문자가 같으면 continue, 다르면 stop
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    # 반복문을 다 돌았으면 팰린드롬이 맞음
    return True


# 앞 뒤로 pop하면서 찾기: 304ms
def is_palindrome_2(s):
    arr = []
    for char in s:
        if char.isalnum():
            arr.append(char.lower())
    
    while(len(arr) > 1):
        if arr.pop(0) != arr.pop():
            return False
    
    return True


# dequeue을 이용하여 앞뒤로 pop: 52ms
def is_palindrome_3(s):
        arr = deque()
        for char in s:
            if char.isalnum():
                arr.append(char.lower())
        
        while(len(arr) > 1):
            if arr.popleft() != arr.pop():
                return False
        
        return True


# 정규 표현식을 이용: 40ms
def is_palindrome_4(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]



s = "A man, a plan, a canal: Panama"
print(is_palindrome_3(s))