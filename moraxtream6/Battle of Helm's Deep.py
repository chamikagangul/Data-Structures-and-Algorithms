O, C, S, B = map(int,input().strip().split())
L, m, n = map(float,input().strip().split())
m,n = int(m),int(n)
K1, K2, K3, K4 =  map(float,input().strip().split())

helth = L +(B*K1 + S*K1/2) * n

x,y = 0,0
S_w = S-x
S_c = x
B_c = B-y
B_w = y


S = S_w+B_w/2



d_us=0
d_en=0
for i in range(m-n):
    print(O,S)  
    O, S= O - S*K2, S - O*K3
    helth+=( S_c * K1/2 + B_c*K1)
    helth-=C*K4
