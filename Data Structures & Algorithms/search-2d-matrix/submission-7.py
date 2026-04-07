class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on rows
        # then do binary search on columns
        top = 0
        bottom = len(matrix) - 1
        row = -1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        row = (top + bottom) // 2
        left = 0
        right = len(matrix[row]) - 1
        col = -1
        while left <= right:
            col = (left + right) // 2
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = col + 1
            else:
                right = col - 1
        

        return False