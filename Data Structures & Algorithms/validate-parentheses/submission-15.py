class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[','}':'{'}

        arr = []
        for i in range(len(s)):
            if s[i] in pairs:
                if arr and arr[-1] == pairs[s[i]]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(s[i])
        
        if not arr:
            return True
        else:
            return False
