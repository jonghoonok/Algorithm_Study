def match(string):
    # 예외처리
    # 별표를 공백으로 치환한 경우보다 짧고, 앞과 뒤가 겹치는 경우가 있을 수 있음
    if len(string)+1 < pattern_len:
        return False

    # 별표 앞부분이 일치하는지 확인
    if front != string[:idx]:
        return False

    # 별표 뒷부분이 일치하는지 확인
    if rear != string[rear_len:]:
        return False

    return True


n = int(input())
pattern = input()
pattern_len = len(pattern)
idx = pattern.index('*')
front = pattern[:idx]
rear = pattern[idx+1:]
rear_len = idx+1 - len(pattern) # 패턴의 rear부분과 같은 길이로 슬라이싱하기 위한 변수

for _ in range(n):
    file_name = input()
    # 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력
    if match(file_name):
        print("DA")
    else:
        print("NE")