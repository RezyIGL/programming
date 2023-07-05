def func(prices: list) -> int:

    leftP = 0
    rightP = 1
    returnVal = 0

    while rightP < len(prices):
        currProfit = prices[rightP] - prices[leftP]
        if prices[leftP] < prices[rightP]:
            returnVal = max(returnVal, currProfit)
        else:
            leftP = rightP
        rightP += 1
    
    return returnVal

price = [7, 6, 3, 2, 5, 1] # 3, cuz 5 - 2 = 3
print(func(price))