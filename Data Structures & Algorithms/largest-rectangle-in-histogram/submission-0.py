class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxS = 0

        for i in range(len(heights)):
            l = i
            r = i+1
            while l >= 0 and heights[i] <= heights[l]:
                    l -= 1
            
            while r < len(heights) and heights[i] <= heights[r]:
                    r += 1
            
            r -= 1
            l += 1
            
            maxS = max(heights[i] * (r-l+1), maxS)
        
        return maxS

            

            