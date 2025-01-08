# NOTES 
# here there are 2 pointers, one for max profit and the other for minimum price, 
# it accesses all the elements in the array and gets the ones which are minimum at min_price and the largest it comes over as max price
# to prevent any errors they are declared as 0 and infinity
# processes all elements, updates the smallest as the min price and similarly takes all, updates for max price 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        min_Price = float('inf')

        for i in prices:
            if i < min_Price:
               min_Price = i
            profit = i - min_Price
            if profit > maxp:
                maxp = profit
        return maxp
