class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        mProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                mProfit = max(mProfit, profit)
            else:
                left = right
            right += 1
        return mProfit

        ## you have left and right, right is finding the highest and the lowest, when i finds the intial lowest, it moves left to it, and right keeps oging to find the highest

        