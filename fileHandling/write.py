f=open("newBk.txt","w")
f.write("The new contet has been added to the file")
f.close()

f=open("newBk.txt","r")
print(f.read())


f.close()