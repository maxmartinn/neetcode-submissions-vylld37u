class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # clarification: given a 9 x 9 board, 
        # each row must be able to contain digits 1-9 without dup;icates
        # each column must be able to contain digits 1-9 without dup;icates
        # each box must be able to contain digits 1-9 without dup;icates



        # brute force

        # check each row and see if theres duplicate values using a set
        # check each column and see if theres duplicate values using a set

        # check each box using iteration techniques

        # if at any moment there is a duplicate return false

        # optmized solution:

        # given a row and column pair add to row, column and box set at once. at any moment there is a duplicate return false

        # plan:

        # iterate through each cell add value to row, columnm  and box set
        # if at anymoment the value already exist in any of the 3 sets then return false

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rowSet[r] or
                   board[r][c] in colSet[c] or
                   board[r][c] in boxSet[(r // 3, c // 3)]):
                   print(rowSet)
                   print(colSet)
                   print(boxSet)
                   return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxSet[(r // 3, c // 3)].add(board[r][c])
        return True



