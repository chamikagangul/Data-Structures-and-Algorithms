stock_prices = [310,315,275,295,260,270,290,230,255,250]

def getMaxProfit(X):
    MAX_PROFIT= 0
    LOW = float('inf')
    for price in X:
        if(LOW>price):
            LOW = price
        
        MAX_PROFIT = max(MAX_PROFIT,price-LOW)
    return MAX_PROFIT

profit =  getMaxProfit(stock_prices)

print(profit)

