class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0 

        while len(prices) > right:
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right 
            right += 1
        return maxProfit






        ## notes:
        # - each value in the array represents a day
        # two goals, 1: choose a day ~ i, 2: sell at the highest day possbile, if there is none higher, not really understanding the 0 part of the question