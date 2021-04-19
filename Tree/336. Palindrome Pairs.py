class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    # 뒤집은 단어를 트라이에 삽입
    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_id = index        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
