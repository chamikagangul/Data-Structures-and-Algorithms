game = [2,4,1,1,0,2,3]

MAX = 0
c = 0
for i in range(len(game)):
    if(MAX<i):
        print("false")
        break
    if(MAX < i + game[i]):
        MAX = i + game[i]
        c+=1
else:
    print("true",c)
