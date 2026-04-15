class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.neighbors = dict() # {char : charNode}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for i, c in enumerate(word):
            node = TrieNode(c)
            if i == len(word) - 1:
                node.isEnd = True
            if c in curr.neighbors:
                curr.neighbors[c].isEnd |= node.isEnd
            else:
                curr.neighbors[c] = node
            curr = curr.neighbors[c]
            

    def search(self, word: str) -> bool:
        curr = self.head
        for i, c in enumerate(word):
            if c in curr.neighbors:
                curr = curr.neighbors[c]
            else:
                return False
            if i == len(word) - 1:
                return curr.isEnd
        return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for i, c in enumerate(prefix):
            if c in curr.neighbors:
                curr = curr.neighbors[c]
            else:
                return False
            if i == len(prefix) - 1:
                return True
        return False
        
        