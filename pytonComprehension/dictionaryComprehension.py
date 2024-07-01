#listComprehension
#zip function is used to combine two lists or itrables 
roll=[1,2,3,4,5]
name=['bk','sp','am','sk','sg']
myDict={roll:name for roll,name in zip(roll,name) }
print("This is my dictionary:",myDict)