class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set() # because we do not reuse the cells

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):  # we are visiting the same position twice
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            path.remove((r, c)) # returning from this position, no longer looking from it
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False