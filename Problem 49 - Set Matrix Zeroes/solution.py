class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        track_rows = [0] * rows        
        track_cols = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    track_rows[i] = 1
                    track_cols[j] = 1

        for i in range(rows):
            for j in range(cols):
                if track_rows[i] or track_cols[j]:
                    matrix[i][j] = 0

