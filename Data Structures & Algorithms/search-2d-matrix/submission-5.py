class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])
        ROW = len(matrix)

        l = 0
        r = ROW * COLS -1

        while l <= r:
            m = l + (r-l) // 2
            row = m // COLS
            col = m % COLS

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        
        return False