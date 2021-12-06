import itertools
x = ""
n = int(input())
cct = "A"
circuitA = []
circuitB = []
while x != "poB":
    circuit = list(map(str, input().strip().split()))
    if(circuit[0] == "CircuitA"):
        cct = "A"
        continue
    elif(circuit[0] == "CircuitB"):
        cct = "B"
        continue
    
    if(cct == "A"):
        circuitA.append(circuit)
    elif(cct == "B"):
        circuitB.append(circuit)

    x = circuit[0]

 

def evaluateOneCct(cct,INPUT,logicDict):
    
    # print(cct,INPUT)

    for i in range(len(cct)):
        if(len(cct[i])  > 1):
            if(str(cct[i])[:2] == "pi"):
                # cct[i] = INPUT[int(cct[i][2:].strip())]
                cct[i] = "True"
            if(str(cct[i])[:3] == "~pi"):
                
                # cct[i] = "not " + INPUT[int(cct[i][3:].strip())]
                cct[i] = "True"
                # print(cct[i])
        
    
    return cct[0], True


    operation = cct[1]
    if(operation not in ["and","or","xor","nand","nor","xnor", "not", "buf"]):
        return cct[0], True

    if(operation == "xnor"):
        operation = "xor"
        exp = "not " + (" " + operation + " ").join(list(map(str,cct[2:])))
    elif(operation == "nand"):
        operation = "and"
        exp = "not " + (" " + operation + " ").join(list(map(str,cct[2:])))
    elif(operation == "nor"):
        operation = "or"
        exp = "not " + (" " + operation + " ").join(list(map(str,cct[2:])))

    else:
        exp = (" " + operation + " ").join(list(map(str,cct[2:])))

    

    exp = exp.replace('xor', '^').replace('~', 'not ')
    for key in logicDict:
        exp = exp.replace(key, str(logicDict[key]))

    if(operation == "not"):
        exp = "not " + exp
    solution = eval(exp)
    # print(exp, " = ",solution)
    return cct[0], solution

def evaluateCct(circuit,INPUT):
    logicDict = {}
    for cct in circuit:
        # print(cct)
        out, solution = evaluateOneCct(cct[:],INPUT,logicDict)
        logicDict[out] = solution
    # print(logicDict)
    return logicDict


# print(evaluateCct(circuitA,INPUT))

INPUTS = list(itertools.product(["True", "False"], repeat=n))

rslt = []
for INPUT in INPUTS:

    outA = evaluateCct(circuitA,INPUT)    
    outB  = evaluateCct(circuitB,INPUT)
    # print(INPUT, outA["poA"],outB["poB"])
    rslt.append(outA["poA"] == outB["poB"])
    

# print(rslt)
if(rslt.count(True) == len(rslt)):
    print("Identical")
elif(rslt.count(False) == len(rslt)):
    print("Inverse")
else:
    print("None")

# INPUT = ["False", "False", "False", "False"]
# outB  = evaluateCct(circuitB,INPUT)