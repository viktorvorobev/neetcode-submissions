class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                
                if num in rows[row]:
                    return False
                rows[row].add(num)

                if num in cols[col]:
                    return False
                cols[col].add(num)

                square_index = row // 3, col // 3 
                if num in squares[square_index]:
                    return False
                squares[square_index].add(num)

        return True