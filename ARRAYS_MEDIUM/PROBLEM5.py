#STOCK BUY AND SELL

#THE PURPOSE OF STOCK BUY AND SELL IS:
#TO FIND THE MAXIMUM PROFIT BY BUYING AT A LOWER PRICE AND SELLING AT A HIGHER PRICE.

#PROCESS:
#TRAVERSE FROM LEFT TO RIGHT.
#KEEP TRACK OF MINIMUM PRICE SEEN SO FAR.
#CALCULATE PROFIT FOR CURRENT DAY.
#COMPARE WITH MAXIMUM PROFIT.
#UPDATE MAXIMUM PROFIT IF CURRENT PROFIT IS BIGGER.
#CONTINUE TILL END OF ARRAY.
#RESULT BECOMES MAXIMUM POSSIBLE PROFIT.

#FORMULA:
    #PROFIT = SELLING PRICE - BUYING PRICE

#CONDITION:
    #MINIMUM PRICE BEFORE CURRENT DAY
    #THAT GUARANTEES MAXIMUM POSSIBLE PROFIT

#IMPORTANT RULES:
    #BUY FIRST.
    #SELL LATER.
    #ONLY ONE BUY AND ONE SELL ALLOWED.

#IF NO PROFIT POSSIBLE:
    #RETURN 0

#WHY THIS WORKS:
    #SMALLER BUYING PRICE GIVES BIGGER PROFIT.
    #TRACKING MINIMUM PRICE HELPS FIND BEST BUYING DAY.
    #CHECKING PROFIT DAILY GUARANTEES MAXIMUM PROFIT.

#EDGE CASES:
    #PRICES DECREASING -> NO PROFIT
    #SINGLE ELEMENT -> CANNOT SELL
    #ALL SAME PRICES -> PROFIT = 0
    #BEST BUYING DAY MAY COME LATER

#FINAL IDEA:
#KEEP TRACK OF THE MINIMUM PRICE SEEN SO FAR
#AND CONTINUOUSLY CALCULATE THE BEST POSSIBLE PROFIT.
    
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

#USING RECURSION METHOD
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