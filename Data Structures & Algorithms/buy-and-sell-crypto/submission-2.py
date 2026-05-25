class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = i = 0
        
        while i < len(prices):
            curr = prices[i]
            if curr < start and i < len(prices) - 1:
                start = curr
                
            if profit < curr - start:
                profit = curr - start
                
            i += 1
            
        return profit

            