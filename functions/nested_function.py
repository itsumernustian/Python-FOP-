def addition(a,b):
    return a+b
def multiply(x,y):
    sum = addition(x,y)
    return sum * x * y

print(multiply(2,3))

def outFunc(a):
    def innerFunc(b):
        nonlocal a
        a+=1
        return a+b
    print(a)
    return innerFunc


inner = outFunc(3)
print(inner(5))

