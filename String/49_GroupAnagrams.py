def groupAnagrams_1(strs):
    words = dict()
    for element in strs:
        check = ''.join(sorted(element))
        if words.get(check):
            words[check].append(element)
        else:
            words[check] = [element]
    return [word for key, word in words.items()]


# 책의 풀이: IDEA는 나와 같은데 defaultdict를 이용하여 짧다
def groupAnagrams_2(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))