# goal is to find the max profit
# buy and sell on another day after buying stock

arr = [1,2,4,2,5,7,2,4,9,0,9]

def find_max(prices):
    max_profit = float('-inf')
    for i in range(len(prices)):
        if i == len(prices)-1:
            continue
        profit = max(prices[i+1:]) - prices[i]
        if profit > max_profit:
            max_profit = profit
    if max_profit < 0:
        return 0
    return max_profit

def find_max_better(prices):
    buy = 0
    sell = 1
    max_profit = 0
    # two cases either move both or move one
    while sell < len(prices):
        if prices[sell] == 0:
            continue
        profit = prices[sell] - prices[buy]
        print(profit, sell, buy)
        if profit > max_profit:
            max_profit = profit
        if profit > 0:
            sell += 1
        else:
            sell += 1
            buy = sell -1
    print(max_profit)
    return max_profit



find_max_better(arr)