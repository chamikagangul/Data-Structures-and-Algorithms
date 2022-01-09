import math
t = int(input())

for i in range(t):
    x = int(input())
    # if(x==2):
    #     raise Exception("Sorry, no numbers below zero")
    
    
  
        


    SUM = 0
    days = 1
    while(True):
        patiants = days**3
        if(patiants<x):
            SUM = SUM + patiants
            days+=1
        else:
            SUM = SUM + patiants
            break
    # print(days,SUM)

    curing = 0
    cureDays = 0
    while SUM >= curing:
        cureDays += 1
        curing += cureDays**2
       

    print(cureDays-days)

