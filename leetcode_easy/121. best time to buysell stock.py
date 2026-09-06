class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            curr_profit = price - min_price 

            if curr_profit > max_profit:
                max_profit = curr_profit

            if price < min_price:
                min_price = price

        return max_profit

 
        