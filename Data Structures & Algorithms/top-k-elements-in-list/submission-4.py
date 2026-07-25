class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            else:
                count[num] += 1
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res