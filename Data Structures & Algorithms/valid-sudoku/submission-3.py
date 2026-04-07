class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for loop that iterates through the board

        # digit isnt in row 
        # digit isnt in column
        # digit isnt in box

        # i, j 

        # rowHashmap = {} # (rowIndex: set())
        # colHashmap = {} # (colIndex: set())

        # boxHashmap = {} # (boxIndex: set()), where boxIndex = (rowIndex // 3, colIndex // 3)

        rowMap = dict()  # (rowIndex: set())
        colMap = dict() # (colIndex: set())
        boxMap = dict() # (boxIndex: set()), where boxIndex = (rowIndex // 3, colIndex // 3)
        for rowIndex in range(9):
            for colIndex in range(9):
                value = board[rowIndex][colIndex] 
                if value.isnumeric():
                    valueInRow = rowIndex in rowMap and value in rowMap[rowIndex]
                    valueInCol = colIndex in colMap and value in colMap[colIndex]
                    boxIndex = (rowIndex // 3, colIndex // 3)

                    valueInBox = boxIndex in boxMap and value in boxMap[boxIndex]

                    if valueInRow or valueInCol or valueInBox:
                        return False
                    rowMap[rowIndex] = rowMap.get(rowIndex, set()).union(value)
                    colMap[colIndex] = colMap.get(colIndex, set()).union(value)
                    boxMap[boxIndex] = boxMap.get(boxIndex, set()).union(value)
        return True






