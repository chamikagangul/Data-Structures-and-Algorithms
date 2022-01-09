s = "".join(input().strip().split())

n = int(len(s)**0.5)+1
x = []
if(len(s) == int(len(s)**0.5) **2):
    n = n -1
   
    for i in range(n):
        x.append(s[i::n])

else:
    for i in range(n):
        # print(s[i::n])
        x.append(s[i::n])

print(" ".join(x))