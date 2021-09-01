#Maximum profit will equal to the difference between all consecutive peaks and valleys
#Why we don't skip peaks? For eg. [7,1,5,3,6,4] 
#It might seem that buying at day 2 (1) and selling at day 5 (6) will result it 5, but it will ALWAYS be less than the consecutive differences
#of peaks buy day 2(1), sell day 3(5) then buy day 4(3) sell day 5(6) [5-1 + 6-3 = 7 > 5]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Edge case
        if len(prices) == 1: return 0 
        
        maxProfit = 0 #0 will be maxProfit for decreasing arrays (transactions would be negative)
        
        for i in range(len(prices) - 1):
            if prices[i] <= prices[i + 1]:
                maxProfit += prices[i + 1] - prices[i]
        
        return maxProfit
