class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1
        
        if zeros > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    continue
                else:
                    res[i] = prod

        if zeros == 0:
            for i in range(len(nums)):
                if nums[i] != 0:
                    cur = int(prod/nums[i])
                    res[i] = cur
                
        
        return res