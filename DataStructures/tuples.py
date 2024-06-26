#tuples
bk=('Bhavesh','Aniket','Shreesha','Saniya')
print(type(bk))


ak=tuple(('Abhi','Shruti','Sainath'))

print("The type of ak is:",type(ak))




print("The tuple has :",len(bk)," Elements")



#Access 
print("The first item form the tuple is:",bk[1])
print("The firs item from the last is",bk[-1])
#print(bk[-6])#trying to access the index out of range 
print("The tuples from the range 1 to 3:",bk[1:3])

print("The tuple upto index 3:",bk[:3])
print("The tuple from index 1:",bk[1:])

#Update
#tuples are immutable but we can first convert it into the list and then convert it into tuple again 

tup1=('Bhavesh','Saniya')
tup2=list(tup1)
tup2.append('Aniket')
tup1=tup2


print(tup1)
print(tup2)#the tup2 is now in the form of list 



print(tup1)






#Unpack - taking the values back into the variables 
(friend1,friend2,friend3)=tup1

print("The friend 1 is :",friend1)
print("The friend 2 is :",friend2)
print("The friend 3 is :",friend3)

#loop 

print("Printing names using for loop:")
for i in tup1:
    print(i)


#using for loop

print("using for loop:")
for i in range(len(tup1)):
    print(tup1[i])



#joins 

tup1+=tup2


#methods 

#count
print("The Bhavesh is present :",tup1.count('Bhavesh')," times in tup1")



#index

print("The bhavesh is present at index",tup1.index('Bhavesh'))