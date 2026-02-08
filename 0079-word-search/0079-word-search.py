class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, index):
            # If we've matched all characters
            if index == len(word):
                return True
            
            # Check boundaries and if current cell matches
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                board[i][j] != word[index]):
                return False
            
            # Mark as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Try all 4 directions
            found = (dfs(i+1, j, index+1) or 
                    dfs(i-1, j, index+1) or 
                    dfs(i, j+1, index+1) or 
                    dfs(i, j-1, index+1))
            
            # Restore the cell
            board[i][j] = temp
            
            return found
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False