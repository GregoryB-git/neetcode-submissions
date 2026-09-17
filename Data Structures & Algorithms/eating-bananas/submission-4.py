class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            middle = (left+right)//2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/middle)
            
            if totalTime <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return res