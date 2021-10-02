x = ['a','c','d','b','b','c','a']

a =
i=0
while(i<len(x)):
    if(x[i] == 'b'):
        j = i+1
        while(j<len(x)):
            if(x[j] == 'b'):
                j+=1
            else:
                break
        # else:
        #     break
            
        x[i:j-len(x)] = x[j:]
    i+=1

    if()
print(x)
