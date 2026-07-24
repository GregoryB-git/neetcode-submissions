from numpy import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2

        merged.sort()

        totlen = len(merged)

        if totlen % 2 == 0:
            return (merged[totlen // 2 - 1] + merged[totlen // 2]) / 2.0
        else:
            return merged[totlen // 2]
        
