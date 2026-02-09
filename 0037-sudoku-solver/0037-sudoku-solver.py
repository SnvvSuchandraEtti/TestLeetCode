class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Initialize sets to track used numbers in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Find all empty cells and populate the sets
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)
                else:
                    empty.append((i, j))
        
        def backtrack(idx):
            if idx == len(empty):
                return True
            
            row, col = empty[idx]
            box_idx = (row // 3) * 3 + col // 3
            
            for num in '123456789':
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_idx]:
                    # Place the number
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_idx].add(num)
                    
                    # Continue with next cell
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_idx].remove(num)
            
            return False
        
        backtrack(0)