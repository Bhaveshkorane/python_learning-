f=open("bk.txt",'a')
f.write("\tThis is appendted content to the exixting file ")
f.close()


f=open("bk.txt","r")
print(f.read())