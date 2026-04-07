class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])


        def capture(r, c):
            if (r not in range(ROWS) or
            c not in range(COLS) or
            board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)


        # capture edge O's
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1] and board[r][c] == "O": # is edge
                    capture(r, c)

        # turn alls O's into X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O": # is edge
                    board[r][c] = "X"

        # turn all T's into O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T": # is edge
                    board[r][c] = "O"
                    