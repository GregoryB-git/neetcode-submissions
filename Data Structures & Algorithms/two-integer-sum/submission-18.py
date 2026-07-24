class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(list)
        for i, n in enumerate(nums):
            hm[n] = i

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hm and hm[diff] != i:
                return [i, hm[diff]]
        
        return diff
