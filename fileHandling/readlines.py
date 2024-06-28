f=open("bk.txt",'r')

#reads the single line at time 
print(f.readline())
print(f.readline())
print(f.readline())

f.close()


#reading multiple lines at time 
f=open('bk.txt','r')

content=f.readlines()

print(content)#this will print the list of sentences 

for i in content:#printing one by one line 
    print(i)