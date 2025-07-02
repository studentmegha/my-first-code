#ques 1 count positive numbers
numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0
for num in numbers:
    if num >0:
        positive_number_count +=1
print("Final count of positive number",positive_number_count)


#q2 sum of even numbers up to a given number n.
 
n = 10 
sum_even = 0

for i in range(1,n+1):
    if i %2 ==0:
        sum_even +=1
print("Sum of even number:,",sum_even)

#q3 multiplication table printer,
#problem : Print the multiplication table for a given number up to 10 but skip the fifth iteration 

number =3

for i in range (1,11):
    print(number, 'x',i ,'=',number*i )

    


