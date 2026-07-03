#without lambda
num=1,2,3,4
def square(x):
    return (x*x)

sqr=list(map(square,num))
print(sqr)

#with lambda
num=1,2,3,4
sqr=list(map(lambda x:x*x,num))
print(sqr)
