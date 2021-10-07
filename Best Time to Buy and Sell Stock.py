class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, prices and prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                mx = max(mx, prices[i]-mn)
            else:
                mn = min(mn, prices[i])
        return mx
""""
Runtime: 1008 ms, faster than 77.33% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 52.53% of Python3 online submissions for Best Time to Buy and Sell Stock.
""""
