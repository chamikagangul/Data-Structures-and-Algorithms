def testDecorator(func):
    def inner(*args, **kwargs):
        print(args,kwargs)
        print("before")
        func(*args, **kwargs)
        print("after")
    return inner
 
@testDecorator
def printName(name):
    print("My name is",name)


printName("chamika")