
def process(x):
    for i in range(len(x)):

        
        if x[i]>x[-1]:
            return "".join(sorted(x[:i] + x[i+1:])[::-1]) +x[i]

def getProcessed(s):
    for i in range(len(s)):
        if(i+1>=len(s)):
            return "no answer"
        if(s[i]>s[i+1]):
            
            x = process(s[:i+2]) + s[i+2:]
            return x[::-1]
        # for j in range(1,len(s[0:i])):
        #     if(j!=0 or i!=j or s[0:j] != s[j:i]):           
        #         if("".join(sorted(s[0:j])) == s[0:j] and "".join(sorted(s[j:i])) == s[j:i][::-1] and s[0:j] > s[j:i]):
        #             # print(f"debug:---- {s}", s[0:j],s[j:i])
        #             r = s[j:i]+s[0:j] + s[i:]
        #             return r[::-1]
    return "no answer"

T = int(input().strip())
for t in range(T):
    s = input()[::-1]
    print(getProcessed(s))
    