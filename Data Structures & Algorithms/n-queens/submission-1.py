class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        posDiagSet = set()
        negDiagSet = set()
        colSet = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in colSet or (row + col) in posDiagSet or (row - col) in negDiagSet:
                    continue
                colSet.add(col)
                posDiagSet.add(row + col)
                negDiagSet.add(row - col)
                board[row][col] = "Q"
                backtrack(row + 1)

                colSet.remove(col)
                posDiagSet.remove(row + col)
                negDiagSet.remove(row - col)
                board[row][col] = "."
        backtrack(0)
        return res