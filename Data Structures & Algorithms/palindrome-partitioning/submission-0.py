class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []

        def backtracking(i):
            if i >= len(s):
                res.append(current.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    current.append(s[i:j+1])
                    backtracking(j + 1)
                    current.pop()
        
        backtracking(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
            
