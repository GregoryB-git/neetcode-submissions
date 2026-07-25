class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnums = []
        for i, n in enumerate(nums):
            cnums.append([n, i])
        cnums.sort()

        i = 0
        j = len(nums) - 1

        while i < j:
            curr = cnums[i][0] + cnums[j][0]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                resi = min(cnums[i][1], cnums[j][1])
                resj = max(cnums[i][1], cnums[j][1])
                return [resi, resj]
        return []