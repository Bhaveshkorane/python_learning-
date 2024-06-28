#raising the error in the python 
# x="hello Bhavesh"
# if not type(x) is int:
#     raise TypeError("The only accepted type is int ")



x=10
y=0
try:
#    if(y==0):
#     raise ZeroDivisionError("The devide by zero error......")
    x=x/y
except ZeroDivisionError as e:
   print(e)
else:
    print("The value entered is of type int ")