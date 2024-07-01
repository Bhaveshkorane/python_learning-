#this is for lambda function 

r = lambda a:a*a
print(r(5))

def myfun(n):
    return lambda a:a*n

doubler=myfun(2)
print(doubler(11))

tripler=myfun(3)
print(tripler(11))


#lambda addition

x=lambda a,b,c:a+b+c
print(x(2,5,8))