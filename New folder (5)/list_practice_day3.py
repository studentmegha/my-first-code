
#ques1
num =[]
num1 =input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
num4 = input("Enter fourth number: ")
num.append(num1)
num.append(num2)
num.append(num3)
num.append(num4)
print("The numbers you entered are: ", num)


#2reverse a list
input=[1, 2, 3, 4, 5]
input.reverse()
print(input) 

#3remove duplicates from a list
input=[1,2,2,3,4,4,5]
no_duplicates = list(set(input))
print(no_duplicates)

#4 sum of  elerment in a list
input = [1, 2, 3, 4, 5]
sum_of_elements = sum(input)
print("Sum of all elements in the list:", sum_of_elements)

input = [1, 2, 3, 4, 5]
max_of_elements = max(input)
print(max_of_elements)

#5 min of all elements in a list

input = [1, 2, 3, 4, 5]
min_of_elements = min(input)
print(min_of_elements)

#6 sort a list
input = [5, 2, 3, 1, 4]
input.sort()
print("Sorted list:", input)
