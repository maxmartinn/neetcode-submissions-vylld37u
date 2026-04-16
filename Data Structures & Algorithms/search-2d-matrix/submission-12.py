class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        # first find the right row that the value is on

        l = 0
        r = ROWS - 1
        while l <= r:
            row = (l + r) // 2
            if matrix[row][0] <= target <= matrix[row][COLS - 1]:
                break
            elif matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1

        l = 0
        r = COLS - 1
        while l <= r:
            cols = (l + r) // 2

            if matrix[row][cols] == target :
                return True
            elif matrix[row][cols] > target:
                r = cols - 1
            else:
                l = cols + 1
        return False 