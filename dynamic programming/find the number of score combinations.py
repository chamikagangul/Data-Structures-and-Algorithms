def findNumberOfCombination1(numbers,expectedSum):
    n1 = numbers[0]
    n2 = numbers[1]
    n3 = numbers[2]

    count = 0
    complz = 0

    for a in range(0,expectedSum//n1+1):
        for b in range(0,expectedSum//n1+1):
            for c in range(0,expectedSum//n1+1):
                complz +=1
                if(a*n1+b*n2+c*n3 == expectedSum):
                    # print(a,b,c)
                    count += 1


    print(count,complz)




def findNumberOfCombination(expectedSum,factors):
    tempDict = {}

    for n in range(0,expectedSum+1):
        tempDict[(0,n)] = 1 if n%factors[0] ==0 else 0

    # print(tempDict)
    for fi in range(1,len(factors)):
        # print(fi)
        for n in range(0,expectedSum+1):
            tempDict[(fi,n)] = tempDict.get((fi-1,n), 0) + tempDict.get((fi,n-factors[fi]),0)
            

    print(tempDict.get((2,12454)))
        
findNumberOfCombination(12454,[2,3,7])

