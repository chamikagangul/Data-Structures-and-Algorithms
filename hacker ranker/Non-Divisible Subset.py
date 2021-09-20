
n,k = list(map(int,input().strip().split()))
s = list(map(int,input().strip().split()))

s_ = []
for i in range(n):
    s_.append(s[i]%k)

c = 0

if(k%2):
    for i in range(1,k//2+1):
        c+= max(s_.count(i),s_.count(k-i))
else:
    for i in range(1,k//2):
        c+= max(s_.count(i),s_.count(k-i))
    
    if(s_.count(k//2)>0):
        c+=1

if(s_.count(0)>0):
    c+=1
print(c)