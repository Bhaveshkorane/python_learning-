#list and its operations 

students=['Shruti','Bhavesh','Abhi','Sai']
print("original list :",students)

#Add at last 
students.append('Aniket')
print("Appended list :",students)

#Extend
newStudents=['Shrutika','Pratibha','Adinath']
students.extend(newStudents)
print("Extended list :",students)

#insert at position
students.insert(0,'Ashwini')
print("Inserted at position list :",students)


#remove element from the list
students.remove('Aniket')
print("list after removing aniket :",students)

students.append('Aniket')

print("list before pop :",students)
#pop
students.pop()#students.pop(0) will remove the element at index 0
print("list after pop :",students)#last element was removed


students.insert(len(students),'Aniket')#here we are adding the element at the end of the list 
print("list after adding at the end :",students)

#sort
print('Before soring the elements :',students)
students.sort()
print('After sorting the elements :',students)

#count
print('The number of times Bhavesh present in the list is:',students.count('Bhavesh'))


#reverse sort
print("Reverse sorting the elements of the list:",students.sort(reverse=True))
#reversing the reversed list
print('Before reverse:',students)
students.reverse()
print('After reverse:',students)

#copy the old list into the new list 
newStudentsList=students.copy()
print('The new list is as follows:',newStudentsList)

#clear the list
students.clear()
print('after clearing the list :',students)


#list comprehension
bhavesh=[x**2 for x in range(10)]
print(bhavesh)


print([(x,y) for x in [1,2,3,4] for y in [4,5,6] if(x!=y)])