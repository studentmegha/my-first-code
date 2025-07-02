#for loops
nums = [ 1,2,3,4,5]

for val in nums:
    print(val)

    vaggies = [ "potatato", "brinjal","ladyfinger", "cucumber"]

for val in vaggies:
    print(val)

tup  =(1,2,3,4,5,6,7,8,9)

for num in tup :
    print(num)

str = "apna college"

for char in str :
    print(char)


str = "apnacollege"

for char in str :
    if(char == 'o'):
        print ("o found")
        break
    print(char)

else: # agr else ki jagh and ya or kuch hota to ange ka print hokar aata jarur
    print("END")


#ques

nums = [ 1,4,9,16,25,36,49,64,81,100]
for el in nums :
    print(el)

#q2
nums = [ 1,4,9,16,25,36,49,64,81,100 ]
idx = 0
x = 36
for el in nums:
    if (el == x ):
        print("number found at idx ", idx)
        break
    idx +=1

print(range(5))

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

seq = range(10)
for i in seq :
    print(i)

for i in range(10):
    print(i)

for i in range(2,10):
    print(i) # range (start,stop)

for i in range(2,10,2):#range(start,stop,step):
    print(i)

# to print even numbers

for i in range(2,100,2):
    print(i)

#print the numbers 1 to 100
for i in range (1,101):
    print(i)

for i in range (100 ,0,-1):
    print(i)

# multiplication number of n
n =2
for i in range (1,11):
    print(n*i)

#pass stetment

for i in range (5):
 pass
    #empty

 print("some useful work")

 #wap to find sum of first n natural numbers . 
 n = 5 
 sum = 0
 for i in range (1,n+1):
     sum +=i
print("total sum =",sum)

n = 7
sum = 0
for i in range (1,n+1):
     sum +=i
print("total sum =",sum)

#wap to find the factorialk of first n mumbers

n = 2
fact = 1
for i in range(1,n+1):
    fact*=i

print("factorial =", fact)


