stock_prices = [310,315,275,295,260,270,290,230,255,250]
stock_prices =[12,11,13,9,12,8,14,13,15]
#My method time - O(n) space - O(1)
def getMaxProfit(X):
    MAX_PROFIT= 0
    LOW = float('inf')
    for price in X:
        if(LOW>price):
            LOW = price
        
        MAX_PROFIT = max(MAX_PROFIT,price-LOW)
    return MAX_PROFIT

def getMaxProfit2(X):
    MAX_PROFIT= 0


    C_LOW_i = 0
    HIGH_i = 0
    LOW = float('inf')
    for i in range(len(X)):
        price = X[i]
        if(LOW>price):
            LOW_i= i
            LOW = price
        
        if(MAX_PROFIT<=price-LOW):
            C_LOW_i = LOW_i
            HIGH_i = i
            MAX_PROFIT = price-LOW
    M = max(getMaxProfit(X[:C_LOW_i]) , getMaxProfit(X[C_LOW_i:HIGH_i][::-1]) ,getMaxProfit(X[HIGH_i:]) )
    return MAX_PROFIT+M


# profit =  getMaxProfit2(stock_prices)
# print(profit)


#book method time - O(n) space - O(n)

def getMaxLossArray(X):
    LossArray = []
    MAX_LOSS= 0
    MAX = -float('inf')
    for price in X:
        MAX = max(MAX,price)       
        MAX_LOSS = max(MAX_LOSS,MAX-price)
        LossArray.append(MAX_LOSS)
    return LossArray

def findProfitArrray(X):
    profitArray =[]
    MAX_PROFIT= 0
    LOW = float('inf')
    for price in X:
        if(LOW>price):
            LOW = price
        MAX_PROFIT = max(MAX_PROFIT,price-LOW)
        profitArray.append(MAX_PROFIT)
    return profitArray

def MaxProfit(X,Y):
    MAX_PROFIT = 0
    for x,y in zip(X,Y):
        MAX_PROFIT = max(MAX_PROFIT,x+y)
    return MAX_PROFIT
X = findProfitArrray(stock_prices)

Y = getMaxLossArray(stock_prices[::-1])[::-1]

print(MaxProfit(X,Y))


