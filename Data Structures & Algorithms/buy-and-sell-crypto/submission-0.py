class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    res.append(prices[j] - prices[i])
        res.sort(reverse=True)
        if res:
            return res[0]
        return 0