class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left = 0
        right = num_cols * num_rows - 1
        while left <= right:
            try_number = (left + right) // 2
            try_col = try_number % num_cols
            try_row = try_number // num_cols
            try_val = matrix[try_row][try_col]
            if try_val == target:
                return True
            if try_val < target:
                left = try_number + 1
            else:
                right = try_number - 1

        return False