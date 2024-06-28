#excepton handing 
x=10
try:
    print(x)
except NameError:
    print('the x is not defined name error')
except :
    print("There is another error ")
else:
    print("the else block means there is no error")

finally:
    print("The finally block gets executed always")