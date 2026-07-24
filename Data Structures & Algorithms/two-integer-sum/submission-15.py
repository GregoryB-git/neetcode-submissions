class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tnums = []
        for i, num in enumerate(nums):
            tnums.append([num, i])
        
        l = 0
        r = len(nums) - 1
        
        tnums.sort()
        while l < r:
            curr = tnums[l][0] + tnums[r][0]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [min(tnums[l][1], tnums[r][1]),
                        max(tnums[l][1], tnums[r][1])]
        return []