q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    container = []

    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))

    COL = []
    ROW = []
    for i in range(n):
        sum_col = 0
        sum_row = 0
        for j in range(n):
            sum_row+=container[i][j]
            sum_col+=container[j][i]
        ROW.append(sum_row)
        COL.append(sum_col)

    COL.sort()
    ROW.sort()

    for i in range(n):
        if(COL[i]!=ROW[i]):
            print("Impossible")
            break
    else:
        print("Possible")




