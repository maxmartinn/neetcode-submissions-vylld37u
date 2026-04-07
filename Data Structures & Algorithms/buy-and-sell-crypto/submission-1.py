class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given a list of prices where prices[i] repersents the price of NeetCoin on the ith day

        # choose a single day to buy one NeetCoin and choose one day to sell it

        # return the maximum profit that can be achieved from neet coin

        # minimum profit is 0 where no transactions are made

        # naive solution:

        # iterate for each index in prices:
        #   iterate again for each price after the current index:
            # see if any profit is made by buying and then selling
            #   update profit to the maximum value

        # optimal solution:

            # repated work checking for the smallest price after each iteration

        # plan

            # assume each index is the lowest price, but also consider selling the price

            # store profit and lowest as seperate variables

            # try to sell the stock by subtracting current index by the lowest

            # now see if the latest stock is the new lowest price

        profit = 0
        lowest = float("inf")

        for p in prices:
            profit = max(profit, p - lowest)
            lowest = min(lowest, p)
        return profit

        """
        
        Input: prices = [10,1,5,6,7,1]
                                       p

        Output: 6

        profit = 6
        lowest = 1
        
        """
