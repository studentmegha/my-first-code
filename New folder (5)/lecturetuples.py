tup=(1,3,4,2,5)
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[1:4])
print(tup[1:4:2])


tup=()
print(tup)
print(type(tup))
tup=(1,) # Tuple with one , and if you don't put a comma, it will be considered an int , comma cumpulsury h chahe hum string likhe 
#for example
#tup=(hello,) # this is a tuple with one comma.
print(tup)
print(type(tup))


tup=(1,2,3,4,5) # tuple with multiple elements , to last me (,) ki jarurat nhi hoti h lekin lagana h to laga sakte h
print(tup)

tup=(1,2,3,4,2,5)
print(tup.count(2)) # count the number of times 2 appears in the tuple
print(tup.index(2)) # index of the first occurrence of 2 in the tuple
print(tup.index(5)) # index of the first occurrence of 5 in the tuple



#lets practice some more ques
#1=  WAP to ask to enter names of 3 favourite movies and store them in a l

movies =[]
mov1 = input("Enter your first favourite movie: ")
mov2 = input("Enter your second favourite movie: ")
mov3 = input("Enter your third favourite movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your favourite movies are: ", movies)



list1 =[1,"abc","abc",1]
copy_list1 = list1.copy()  # creates a shallow copy of the list
copy_list1.reverse()  # reverses the copy of the list
if(copy_list1==list1):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")


list2 = [1,2, 1]
copy_list2 = list2.copy()  # creates a shallow copy of the list
copy_list2.reverse()  # reverses the copy of the list
if(copy_list2==list2):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")


list=[2,3,2]
list.copy()
list.reverse()
list.reverse().copy()
if(list==list.reverse().copy()):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
    










