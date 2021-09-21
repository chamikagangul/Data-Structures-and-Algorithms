x = [9,9,9]
 
i = 23535543
p=-1
while(i):
    if(len(x)<abs(p)):
        x =[0]+ x
    j = (x[p] +i)//10
    x[p] = (x[p] +i)%10
    p-=1
    i = j

print(x)