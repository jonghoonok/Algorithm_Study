# 내 풀이: 중복을 발견하면 해당 지점으로 돌아가서 다시 딕셔너리를 이용해 중복 체크
# 상당히 느림
def lengthOfLongestSubstring_1(s: str) -> int:
    result = 0
    sub_string = {}
    temp = 0
    i = 0
    while i < len(s):
        if s[i] not in sub_string:
            sub_string[s[i]] = i
            temp += 1
        else:
            i = sub_string[s[i]] + 1
            sub_string = {}
            sub_string[s[i]] = i
            result = max(result, temp)
            temp = 1
        i += 1
    
    result = max(result, temp)
    return result

s = "pwwkew"
print(lengthOfLongestSubstring(s))


# 슬라이딩 윈도우 + 투 포인터
def lengthOfLongestSubstring(s: str) -> int:
        used = {}
        max_length = start = 0

        # 오른쪽 포인터 index는 계속 전진
        for index, char in enumerate(s):
            # 이미 등장한 문자를 만나면
            if char in used and start <= used[char]:
                # 왼쪽 포인터의 위치를 등장한 문자 바로 오른쪽으로 이동
                start = used[char] + 1
            # 처음보는 문자라면
            else:
                # 중복없는 가장 긴 부분 문자열의 길이를 갱신
                max_length = max(max_length, index - start + 1)
            
            # 현재 문자의 위치를 갱신
            used[char] = index
        
        return max_length