class Solution:
    def binsearch(self, l, r, nums, target):
            if l > r:
                return -1
            
            m =(l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return self.binsearch(m+1, r, nums, target)
            else:
                return self.binsearch(l, m-1, nums, target)
            
    def search(self, nums, target):
        return self.binsearch(0, len(nums)- 1, nums, target)
