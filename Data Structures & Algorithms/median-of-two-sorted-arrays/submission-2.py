class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        totLen = len(merged)
        
        if totLen % 2 == 0:
            return (merged[totLen // 2 - 1] + merged[totLen // 2]) / 2.0
        else:
            return merged[totLen // 2]