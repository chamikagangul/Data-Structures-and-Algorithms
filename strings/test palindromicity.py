s = "Able was I, erre I saw Elba!"
s2 = "A @#$%^&*()man,a plan, a canal/ Panama."


def isPalindrom(x):
    i=0
    j=1
    lenX = len(x)
    while(i<lenX-j):
        while(not x[i].isalnum() and i<lenX-j):
            i+=1
        while(not x[lenX-j].isalnum() and i<lenX-j):
            j+=1
        # print(x[i].lower(),x[lenX-j].lower())
        if(x[i].lower()!=x[lenX-j].lower()):
            return False
        i+=1
        j+=1
    return True


print(isPalindrom(s2))