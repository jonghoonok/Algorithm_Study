# 공백을 기준으로 문자열을 단어단위로 뒤집어 줌
def reverse_word(word):
    result = ''
    j = 0
    for i in range(len(word)):
        if word[i] == ' ':
            result += word[j:i][::-1]
            result += ' '
            j = i+1
    result += word[j:][::-1]

    return result


# 태그와 태그 사이의 문자열을 단어단위로 뒤집어 줌
def reverse_tag(string):
    left = string.find('<')
    # case 1 : 태그가 하나도 없음
    if left == -1:
        return reverse_word(string)

    # case 2 : 중간에 태그가 있음
    result = ''
    while string and left != -1:
        right = string.find('>')
        result += reverse_word(string[:left])
        result += string[left:right+1]
        string = string[right+1:]
        left = string.find('<')

    # while문이 끝났으면 문자열을 다 뒤집었거나 태그 뒤에 단어가 하나 남았음
    if string:
        result += reverse_word(string)

    return result

string = input()
print(reverse_tag(string))