from random import randint


def negetion(n):
    return (1 << 8) - 1 - n


n = int(input())
if (n>0):
    a = {}
    val1 = 0
    val2 = 0

    for i in range(n):
        a["pi"+str(i)] = randint(0, 127)
    # print(a)

    while(1):
        f = input().split()
        if (len(f) == 1):
            continue

        elif (len(f) == 3):
            out, operation, operation1 = f
            if (operation1[0] == '~'):
                operation1 = operation1[1:]
                val1 = negetion(a[operation1])
            else:
                val1 = a[operation1]
            if(operation == "not"):
                a[out] = negetion(val1)
            elif (operation == "buf"):
                a[out] = val1

        else:
            out, operation, operation1, operation2 = f
            if ((operation1[0] == '~') or (operation2[0] == '~')):
                if (operation1[0] == '~'):
                    operation1 = operation1[1:]
                    val1 = negetion(a[operation1])
                else:
                    val1 = a[operation1]
                if (operation2[0] == '~'):
                    operation2 = operation2[1:]
                    val2 = negetion(a[operation2])
                else:
                    val2 = a[operation2]
            else:
                val1 = a[operation1]
                val2 = a[operation2]

            if (operation == "or"):
                a[out] = val1 | val2
            elif(operation == "and"):
                a[out] = val1 & val2
            elif(operation == "xor"):
                a[out] = val1 ^ val2
            elif(operation == "xnor"):
                a[out] = negetion(val1 ^ val2)
            elif(operation == "nor"):
                a[out] = negetion(val1 | val2)
            elif(operation == "nand"):
                a[out] = negetion(val1 & val2)

        if (out == "poB"):
            break


    # print(a)

    if (a["poA"] == a["poB"]):
        print("Identical")
    elif (a["poA"] == negetion(a["poB"])):
        print("Inverse")
    else:
        print("None")
else:
    print("None")