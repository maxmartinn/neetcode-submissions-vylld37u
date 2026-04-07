class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # iterate through all possible starting combinations in the board

        # check all directions and update i

        # check if the current i is in the path and if the current pos matches index in word
        # return False if other wise

        # if i is equal to the length of the word then return true

        visit = set()
        ROWS = len(board)
        COLS = len(board[0])
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if not (r in range(ROWS) and c in range(COLS)):
                return False
            if (r, c) in visit or board[r][c] != word[i]:
                return False
            visit.add((r,c))
            res = (backtrack(r - 1, c, i + 1) or
            backtrack(r + 1, c, i + 1) or
            backtrack(r, c - 1, i + 1) or
            backtrack(r, c + 1, i + 1))
            visit.remove((r, c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False