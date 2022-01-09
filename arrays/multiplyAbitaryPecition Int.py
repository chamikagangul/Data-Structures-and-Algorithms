x="9932424235743853278943333375835735732785778832587737571385935798145493487770349875849348754839847543422"
y="231254839783948768398408432785929574985692832568525637378357256756327562353493412421099849210481092740173599271313"
print(int(x)*int(y))


x = list(map(int,list(x)))
y = list(map(int,list(y)))

def Mul(A,B):
    
    if(len(A)<len(B)):
        A,B =B,A
    MAX = len(A)
    MIN = len(B)     

    y = [0 for _ in range(MIN+MAX)]

    for i in range(MAX):
        for j in range(MIN):
            
            y[i+j] += A[-(i+1)] * B[-(j+1)] 
            if(y[i+j]>=10):
                
                y[i+j+1] += y[i+j]//10
                y[i+j] = y[i+j]%10
    return y[::-1]
print(x,y)

print("".join(str(p) for p in Mul(x,y)))
