import sys
import re
def getdDstance(A,B):
    def computeTable(A_index,B_index):
        # print(A_index,B_index)
        if(table[A_index-1][B_index-1] == -1):
            if(A[0:A_index]==B[0:B_index]):
                table[A_index-1][B_index-1] =  0
            elif(A_index==0):
                table[A_index-1][B_index-1] =  B_index + 1
            elif(B_index == 0):
                table[A_index-1][B_index-1] =  A_index + 1
            
            elif(A[A_index-1] == B[B_index-1]):
                table[A_index-1][B_index-1] =  computeTable(A_index-1,B_index-1) 
            else:
                table[A_index-1][B_index-1] = 1+ min(computeTable(A_index-1,B_index-1) ,computeTable(A_index-1,B_index) , computeTable(A_index,B_index-1))
        return table[A_index-1][B_index-1]

    table = [[-1] * len(B) for _ in range(len(A))]
    
    computeTable(len(A),len(B))
    
    print(table, table[-1][-1])
a = "තරනය"

b = "තරණය"

a = re.sub(r'\W+', '', a)
b = re.sub(r'\W+', '', b)

print(a,b)
sys.setrecursionlimit(2700)


getdDstance(a,b)
