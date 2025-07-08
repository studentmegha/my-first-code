#recursion function
def show (n):
    if(n==0):   #if this deleate so program infinity time a jayega
        return
    print(n)
    show(n-1)
    print("END")

show(3)# 5,4,n = 4-1,3,3-1

def fact(n):
    if( n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(6)) 

#q1 writw a recursion function to calculate the sum pf a first n natural numbers
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
    sum = calc_sum(4)
print(sum)

