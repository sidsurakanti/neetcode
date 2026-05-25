class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        profit = 0
        i = 1
        
        while i < len(prices):
            curr = prices[i]
            
            if curr < start:
                start = curr
                
            if profit < curr - start:
                profit = curr - start
                
            i += 1
            
        return profit

            