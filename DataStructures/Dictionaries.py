#Dictionaries


myDict={
"name":"Bhavesh",
"age":22,
"gender":"M",
"height":174,
"weight":80

}

#accessing items 
print(myDict["name"])
print(myDict.get("age"))

#Dictionary keys 
x=myDict.keys()
print(type(x))

print(x)
for i in x:
    print(i)

#modifying the item into the dictionary 
myDict["address"]="Belebhat"


#Dictionary values and items 
print(myDict.values())

print(myDict.items())


#change the itms 
myDict.update({"address":"Chandgad"})

print(myDict)

#Accessing by looping 
for k,v in myDict.items():
    print(k,v)


for i in sorted(myDict):
    print(myDict.get(i))





