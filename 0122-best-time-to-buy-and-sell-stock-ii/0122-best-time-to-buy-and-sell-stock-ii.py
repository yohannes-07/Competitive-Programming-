class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            
            if price > min_price:
                max_profit += (price - min_price)
                min_price = price
            
             
        return max_profit