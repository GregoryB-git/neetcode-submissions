class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num
        
        if zeros > 1:
            return [0] * len(nums)
        
        res = []
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for i in range(len(nums)):
                res.append(prod // nums[i])
        
        return res