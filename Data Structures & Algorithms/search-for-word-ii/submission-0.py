class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the full word at end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # mark found so no duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = ch  # restore

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res