import sys
import re

def printTable(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '| ' + '  |  '.join('{{:{}}}'.format(x) for x in lens) + ' |'
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def getdDstance(A,B):
    
    table = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]

    table[0][0] = 0

    for i in range(len(A) + 1):
        table[i][0] = i
    for j in range(len(B) + 1):
        table[0][j] = j

    for i in range(len(A)):
        for j in range(len(B) ):
            if(A[i]==B[j]):
                table[i+1][j+1] = table[i][j]
            else:
                substituteLast = table[i][j]
                addLast = table[i][j+1]
                deleteLast = table[i+1][j]

                minDistance = min(substituteLast , addLast, deleteLast)

                table[i+1][j+1] = 1+ minDistance



    printTable(table)
    print(table[-1][-1])
a = "chamika"

b = "cham5ika"

a = re.sub(r'\W+', '', a)
b = re.sub(r'\W+', '', b)

print(a,b)
sys.setrecursionlimit(2700)


getdDstance(a,b)
