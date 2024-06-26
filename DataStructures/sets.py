#sets

thisset={'Bhavesh','Aniket','Abhi','sai','Aniket'}

#printing the elements of the this set 
print(thisset)

#accessing all the elements of the set
for i in thisset:
    print(i)

#viewing if the element is present in the set or not 

print('Bhavesh' in thisset)
print('Bhavesh' not in thisset)


#Add items into the set
thisset.add('saniya')
thisset.add('soumya')

print("The set after adding new items ",thisset)


anotherset={1,2,3,4,False}

thisset.update(anotherset)
print("After adding new set to older:",thisset)



#removing item from the list  remove() discard()

#if the item is known to present in the set we can use remove 
thisset.remove('soumya')

#if the item is not konwn to have in the list them we can discard it willnot raise the error 
thisset.discard('shruti')

print("The set after after removing soumya ",thisset)



#joining sets
#union
print('This is union :',thisset.union(anotherset))

#intersection 
print('This is intersection:',thisset.intersection(anotherset))


#difference
print('This is difference:',thisset.difference(anotherset))


#symmetric_difference
print('This is symmetric difference :',thisset.symmetric_difference(anotherset))



