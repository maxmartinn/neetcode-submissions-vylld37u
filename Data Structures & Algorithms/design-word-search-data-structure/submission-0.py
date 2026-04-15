class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = dict()
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            if word[i] == ".":
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True
            elif word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False
        return dfs(self.head, 0)