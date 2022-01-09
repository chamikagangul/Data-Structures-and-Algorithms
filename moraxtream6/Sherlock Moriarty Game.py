
for i in range(5):
    n = int(input())
    for i in range(3,n+1,3):
       
        if((n-i)%5==0):
                           
            if(i<n-i):
                print("S"*i + "H"*i)
            else:
                print("S"*i + "H"*(n-i))
            break
    else:
        if(n%5==0):
            print("H"*n)
        else:
            print("Invalid Model Name")