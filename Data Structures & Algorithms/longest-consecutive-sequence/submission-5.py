class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        exp = nums[0]
        res = 0
        streak = 0
        i = 0

        while i < len(nums):
            if nums[i] != exp:
                streak = 0
                exp = nums[i]
            while i < len(nums) and nums[i] == exp:
                i += 1
            
            streak += 1
            exp += 1
            res = max(res, streak)

        return res