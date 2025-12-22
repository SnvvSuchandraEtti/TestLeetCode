class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        
        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            
            for col in range(n):
                d1 = row - col
                d2 = row + col
                
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                
                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                
                backtrack(row + 1)
                
                # Remove queen
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)
        
        backtrack(0)
        return result