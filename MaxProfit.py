class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        for p in prices:
            if p < low:
                low = p
            else:
                res = max(p - low, res)
        return res
