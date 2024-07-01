#list comprehension 

newList=[a for a in range(1,101)]
print("This is all numbers form 1 to 100:\n",newList)
print()


newEvenList=[e for e in range(1,101) if e%2==0]
print("This is all even numbers from 1 to 100:\n",newEvenList)


print()
newOddList=[o for o in range(1,101) if o%2!=0]
print("This is all odd numbers list from 1 to 100:\n",newOddList)


print()
newDivBy5_0=[d for d in range(1,101) if d%2==0 and d%5==0]
print("All the numbers divisiable by 5 and 0:",newDivBy5_0)


myList=[a for a in range(1,11) ]
print(myList)


mySqList=[a*a for a in myList]
print(mySqList)

#create the combinations for abcd and 1234
myComboList=[(char,num) for char in "abcd" for num in range(1,5)]
print("\n the combination of the given input is:",myComboList)



#create the combinations for abcd and abcd
myComboList=[(char,num) for char in "aaabcd" for num in "abcd"]
print("\n The combination of the given abcd and abcd is :",myComboList,"",len(myComboList))


#create combo set
myComboSet={(char,num) for char in "aaabcd" for num in "abcd"}
print("\n The combination of the given abcd and abcd is :",myComboSet,"",len(myComboSet))
