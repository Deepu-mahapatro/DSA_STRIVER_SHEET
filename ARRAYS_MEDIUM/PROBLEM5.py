#STOCK BUY AND SELL

#The purpose of Stock Buy and Sell is:
#To find the maximum profit by buying at a lower price and selling at a higher price.

#PROCESS:
#Traverse from left to right.
#Keep track of minimum price seen so far.
#Calculate profit for current day.
#Compare with maximum profit.
#Update maximum profit if current profit is bigger.
#Continue till end of array.
#Result becomes maximum possible profit.

#FORMULA:
    #profit = selling price - buying price

#CONDITION:
    #minimum price before current day
    #That guarantees maximum possible profit

#IMPORTANT RULES:
    #Buy first.
    #Sell later.
    #Only one buy and one sell allowed.

#IF NO PROFIT POSSIBLE:
    #Return 0

#WHY THIS WORKS:
    #Smaller buying price gives bigger profit.
    #Tracking minimum price helps find best buying day.
    #Checking profit daily guarantees maximum profit.

#EDGE CASES:
    #Prices decreasing -> no profit
    #Single element -> cannot sell
    #All same prices -> profit = 0
    #Best buying day may come later
#FINAL IDEA:Keep track of the minimum price seen so far 
#continuously calculate the best possible profit.
    
#USING BRUTE FORCE METHOD
def maxProfit(price):
    #EDGE CASE:
    if len(price)<2:
        return 0
    max_profit=0
    for buy in range(len(price)):
        for sell in range(buy+1,len(price)):
            profit=price[sell]-price[buy]
            max_profit=max(max_profit,profit)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))

#OPTIMAL GREEDY APPROACH
def maxProfit(price):
    #EDGE CASE:
    if len(price)<2:
        return 0
    min_price=price[0]
    max_profit=0
    for i in price:
        #UPDATE MINIMUM PRICE
        min_price=min(min_price,i)
        #CALCULATE PROFIT
        profit=i-min_price
        #UPDATE MAXIMUM PROFIT
        max_profit=max(max_profit,profit)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))


def maxProfit(prices):
    if len(prices) < 2:
        return 0
    def solve(index, min_price, max_profit):
        #BASE CASE
        if index == len(prices):
            return max_profit
        # UPDATE MINIMUM PRICE
        min_price = min(min_price, prices[index])
        # CALCULATE PROFIT
        profit = prices[index] - min_price
        # UPDATE MAXIMUM PROFIT
        max_profit = max(max_profit, profit)
        return solve(index + 1, min_price, max_profit)
    return solve(1, prices[0], 0)
print(maxProfit([7,1,5,3,6,4])) 