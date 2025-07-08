a = 5
b = 10

sum = a+b
print(sum)

def calc_sum(a,b):
     sum = a +b
     print(sum)
     return sum
      #or
calc_sum(5,10)

a = 7
b = 19
sum = a+b
print(sum)
#or
calc_sum(7,19)

#function defination
def calc_sum(a,b): #a amnd b cslled parameters
     return a +b

sum = calc_sum(178,2221) # function call; arguments
print(sum)

def print_hello():
     print("hello")

print_hello()

output = print_hello()
print(output)#output= none

#average of 3 numbers

def calc_avg(a,b,c):
     sum = a+b+c
     avg = sum/3
     print(avg)
     return avg
calc_avg(71,64,95) #76.66

print("apna college") #sep = " "  , automatic space a jayega    #output apnacollege
print("meghayadav") #end = "\n"  #output= meghayadav

print("apna college", end="$ ") #sep = " "
print("meghayadav")  # output = apnacollege meghayadav

def calc_prod(a = 2,b = 5):
     print(a*b)
     return a*b
calc_prod()

def calc_prod(a = 2,b = 5):
     print(a*b)
     return a*b
calc_prod(1)

#wap to print the lenght of list

cities = ["delhi", "gurgaun","noida","pune","mumbai","chennai"]
heroes = [ "thor","ironman","caption america","shaktiman"]


def print_len(list):
     print(len(list))

print_len(cities)#output = 7
print_len(heroes) #output 5
#wap tp print the element of a list in a single line {list is the parameter}

heroes = [ "thor","ironman","caption america","shaktiman"]
def print_len(list):
     print(len(list))

def print_list(list):
     for item in list:
          print(item,end=" ")

print_list(heroes)


#write tp find of n (n is the parameter)
n = 5
def calc_fact(n):
     fact=1
     for i in range(1,n+1):
          fact*=i
          print(fact)
calc_fact(5)


#wap to convert USD to INR
#1doller=83rupee

def converter(usd_val):
     inr_val = usd_val *83
     print(usd_val,"USD =",inr_val,"INR")

converter(1)
converter(10)

#function ques 
     
#write a function to calculate and return the square of a number
def square (number):
    return number**2
result =square(4)
print(result)

#q2 create a function that takes two numbers as parameter and return there sum.
def add(num1,num2):
    return  num1+num2
print(add(5,5))

#q3 write a function multiply thats multuiple two numbers , but also can accept and multiple strings
def multiple(p1,p2):
     return p1*p2
print(multiple(8,9))
print(multiple("a",9))

#q4  create a function that return both the area and circumferenceof a circle gives it radius.

     
     
     
     
     
     
     





