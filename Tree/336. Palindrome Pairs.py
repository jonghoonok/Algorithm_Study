class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def is_palindrome(self, word):
        return word[::] == word[::-1]

    # 뒤집은 단어를 트라이에 삽입
    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            # 이 부분은 잘 모르겠는데 나중에 확인하자
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        
        # 뒤집은 단어가 끝나는 곳에 해당 단어의 index 값을 기입해둠
        # 다른 단어를 root에서부터 탐색했을 때 끝나는 지점의 값이 index라면, index단어+해당 단어는 팰린드롬
        node.word_id = index        

    def search(self, index: int, word: str) -> bool:
        node = self.root
        result = []

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
            
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results