#count = 1
#while count <= 5 :
 #  print("hello")
   # print(i)
    #i+=1
#print("loop ended")

#ques

#print no. from 1 to 100
i = 1
while i<=100: 
    print(i)
    i+=1

#ques2 print no. from 100 to 1

i = 100
while i>=1:
    print(i)
    i-=1

#q3 print the multiplication table of a number n

i = 1 #1 table
while i<=10:
    print(i)
    i+=1

i = 1 # 3 table
while i<=10:
    print(3*i)
    i+=1

#q4 print the element of the following list using loops
#[1,4,9,16,36,49,64,81,100]

#nums = [ 1,4,9,16,36,49,64,81,100]
#idx = 0
#hile idx < len(nums):
  #  print(nums[idx]) #nums[0], nums[1], nums[2]
   # idx += 1

nums = (1,4,9,16,25,36,64,81,100)

x = 36

i = 0 #initialisation
while i < len(nums):
        if nums[i]==x:
             print("FOUND at idx",i)
        else:
             print("finding")
        i+=1



i = 1
while i<=5:
     print(i)
     if(i==3):
          break
     i+=1

print("end of loop")




i = 0
while i <=5:
     if(i ==3):
          i+=1
          continue  #acts as skip
     print(i)
     i +=1

i = 0
while i <=10:
     if(i%2==0):
          i+=1
          continue  #acts as skip
     print(i)
     i +=1

i = 0
while i <=10:
     if(i%2!=0):
          i+=1
          continue  #acts as skip
     print(i)
     i +=1

list = [1,2,3,4,5]

for val in nums :
     print(val)




