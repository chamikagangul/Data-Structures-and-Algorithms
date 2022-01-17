import sys
import re

def printTable(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '| ' + '  |  '.join('{{:{}}}'.format(x) for x in lens) + ' |'
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def getdDstance(A,B):
    def computeTable(A_index,B_index):
        # print(A_index,B_index)
        if A_index < 0:
            return B_index + 1
        if B_index < 0:
            return A_index + 1
 
        if(table[A_index+1][B_index+1] == -1):
            
            if(A[A_index]==B[B_index]):
                table[A_index+1][B_index+1] =  computeTable(A_index-1,B_index-1)
                # print("prefix same : ",A[0:A_index])
            else:
                substituteLast = computeTable(A_index-1,B_index-1)
                addLast = computeTable(A_index-1,B_index)
                deleteLast = computeTable(A_index,B_index-1)

                minDistance = min(substituteLast , addLast, deleteLast)
                
                # if(substituteLast ==minDistance ): print("substituteLast : ",A[A_index-1])
                # elif(addLast == minDistance): print("addLast : ",A[A_index-1])
                # elif(deleteLast == minDistance): print("deleteLast : ",B[B_index-1])

                table[A_index+1][B_index+1] = 1+ minDistance

        return table[A_index+1][B_index+1]

    table = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
    
    computeTable(len(A)-1,len(B)-1)
    printTable(table)
    print(table[-1][-1])
a = "carthorse"

b = "orchestra"

a = re.sub(r'\W+', '', a)
b = re.sub(r'\W+', '', b)

print(a,b)
sys.setrecursionlimit(2700)


getdDstance(a,b)
