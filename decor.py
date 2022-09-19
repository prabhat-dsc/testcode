# decorator function

def outer(func):
    def wrapper(x,y):
        if y==0:
            x,y=y,x
        val=func(x,y)
        return val
    return wrapper
@outer
def div(a,b):
    d=a/b
    return d
z=div(10,10)
print(z)