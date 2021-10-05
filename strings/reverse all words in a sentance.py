def reverseString(s):
    s = s.encode()
    print(s)
    s = bytearray(s)
    print(s)
    s.reverse()

    

    def reverseAWord(s,start,end):
        while(start<end):
            s[start],s[end] =  s[end],s[start]
            start,end = start+1,end-1
        return s
    
    i,j = 0,0
    lenS = len(s)
    
    while(i<lenS and j<lenS):
        # print(s[j])
        if(s[i] == 32):
            i+=1
            j+=1
            continue
        if(s[j] == 32):
            s = reverseAWord(s,i,j-1)
            i = j
            i+=1
        
        j+=1
    s = reverseAWord(s,i,j-1)
    return s
print(reverseString("chamika gangul mahiepala"))
        