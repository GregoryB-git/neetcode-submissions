class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
    
        def binsearch(left, right):
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        result = binsearch(0, pivot - 1)
        if result != -1:
            return result
        
        return binsearch(pivot, len(nums) - 1)