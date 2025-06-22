marks1 = 94.4
marks2 = 87.5
marks3 = 95.5
marks4 = 66.4
marks5 = 45.1

marks = [94.4,87.5,95.5,66.4,45.1]
print(marks)
print(type(marks))

print (marks[0])
print(marks[1])

student = ["karan", 95.4,"Delhi"]
print(student[0])
student[0]="amal" # change possible in lists
print(student)


str = "hello"
print(str[0])



marks=[85,94,76,63,48]
print(marks[1:4])
print(marks[:5])
print(marks[1:])
print(marks[0:2])
print(marks[-3:-1])
print(marks[-5:-1])


list = [2,1,3]
list.append(4)
print(list)


list = [2,1,3]
list.append(4)
list.sort()
print(list)

list = [2,1,3]
list.sort(reverse=True)
print(list)

list = [2,1,3]
list.reverse()
print(list)

list=['a','b','c','d','e']
list.sort()
print(list)
list.append('f')
print(list)
list=['a','b','c','d','e']
list.insert(4,'x')
print(list)
list.insert(3,'x')
print(list)

list = [2,1,3,1]
list.remove(1)  # removes first occurrence of 1
print(list)
list = [2,1,3,1]
list.pop(2)  # removes element at index 2
print(list)
 
list = [2,1,3,1]
list.copy()  # creates a shallow copy of the list
print(list)

list = [2,1,3,1]
list.count(1)  # counts occurrences of 1 in the list
print(list.count(1))

list = [2,1,3,1]
list.__add__([4,5])  # adds another list to the current list
print(list.__add__([4,5]))


