count = 0
def Move(fromTower,toTower,tempTower,n):
    global count
    
    if(n == 0):
        return
    
    Move(fromTower,tempTower,toTower,n-1)
    print(count, "Move - ",fromTower, "->",toTower )
    count+=1
    Move(tempTower,toTower,fromTower,n-1)

Move(1,2,3,4)

print(count)