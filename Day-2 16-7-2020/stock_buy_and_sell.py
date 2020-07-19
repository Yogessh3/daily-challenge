#O(N) Time Complexity / O(1) Space Complexity
def max_profit(stocks):
    maximum_profit=0
    current_profit=0
    total_profit=0
    buyIdx=0
    sellIdx=0
    while(sellIdx<len(stocks)):
        if(stocks[buyIdx]<=stocks[sellIdx]):
            current_profit=stocks[sellIdx]-stocks[buyIdx]
            sellIdx+=1
        elif(stocks[buyIdx]>stocks[sellIdx]):
            total_profit+=maximum_profit
            maximum_profit=0
            buyIdx=sellIdx
            current_profit=stocks[sellIdx]-stocks[buyIdx]
        if(maximum_profit<current_profit):
            maximum_profit=current_profit
    total_profit+=maximum_profit
    return total_profit
stocks=[100,180,260,310,410,25,65,850]
print(max_profit(stocks))

        
