class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        left = 0

        while left < len(s):
            right = left

            while s[right] != '#':
                right += 1
            
            length = int(s[left:right])

            left = right + 1
            right = left + length
            res.append(s[left:right])

            left = right

        return res