class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        arr = []
        
        for c in s:
            if c in pairs:
                if arr and arr[-1] == pairs[c]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(c)
        
        return len(arr) == 0