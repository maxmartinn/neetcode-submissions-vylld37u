class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        # have dictonary to help check row, column and square

        # precompute dictonaries

        # check all rules

        # iterate through the matrix

        # if the element is already in one of the dictonaries, return False

        ROWS = 9
        COLS = 9

        rowDict = defaultdict(set)
        columnDict = defaultdict(set)
        squareDict = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                squareIndex = (r // 3, c // 3)
                digit = board[r][c]
                if digit in rowDict[r]:
                    return False
                if digit in columnDict[c]:
                    return False
                if digit in squareDict[squareIndex]:
                    return False
                if digit != ".":
                    rowDict[r].add(digit)
                    columnDict[c].add(digit)
                    squareDict[squareIndex].add(digit)
        return True


