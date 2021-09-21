n,k = list(map(int,(input().strip().split())))

x,y = list(map(int,(input().strip().split())))

obs =[]
for i in range(k):
    obs.append(list(map(int,(input().strip().split()))))

# reorganiz
def reorganiz(x,y,n):
    obs = [[x,n+1],[n+1,y],[x,0],[0,y]]

    tr = min(n-x,n-y) + 1
    obs.append([x+tr,y+tr])
    tl = min(n-x,y-1) + 1
    obs.append([x+tl,y-tl])

    br = min(x-1,n-y) + 1
    obs.append([x-br,y+br])
    bl = min(x-1,y-1) + 1
    obs.append([x-bl,y-bl])
    return obs

    
obs += reorganiz(x,y,n)

cost = [n,n,n,n,n,n,n,n]

for ob in obs:
    
    d_x,d_y = x-ob[0],y-ob[1]
    if(d_x ==0 and  d_y > 0):
        cost[0] = min(cost[0],d_y)
    elif(d_x == d_y and d_y>0):
        cost[1] = min(cost[1],d_y)
    elif(d_x > 0 and d_y==0):
        cost[2] = min(cost[2],d_x)
    elif(-d_x == d_y and d_y>0):
        cost[3] = min(cost[3],d_y)
    elif(d_x ==0 and  d_y < 0):
        cost[4] = min(cost[4],-d_y) 
    elif(d_x == d_y and d_y<0):
        cost[5] = min(cost[5],-d_y)
    elif(d_x < 0 and d_y==0):
        cost[6] = min(cost[6],-d_x)
    elif(d_x == -d_y and d_y<0):
        cost[7] = min(cost[7],-d_y)

print(sum(cost)-8)