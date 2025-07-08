a = 10
b = 20
sum = a+b
print(sum)

diff = a-b
print(diff)

#function = reduncy decrease, reusibility increase

class Student :
    name = "karan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"


Car1 = Car()
print(Car1.color)
print(Car1.brand)

#default constructors
class Student :
        name = "karan"
        def __init__(self):
             print(self)
             print("adding new student in database..")
             
s1 = Student()
print(s1)

#parameterized constructors
class Student :
        def __init__(self,name,marks):
             self.name = name
             self.marks = marks
             print("adding new student in database..")
             
s1 = Student("Karan",88)
print(s1.name,s1.marks)

s2 = Student("Arjun",69)
print(s2.name,s2.marks)


class Student :
        college_name = "ABC college"
        name = "anomynous"  #class attr

        def __init__(self,name,marks):
             self.name = name  #obj attr > class attr
             self.marks = marks

             def welcome(self):
                   print("welcome students")

             

             
s1 = Student("Karan",88)
print(s1.name,s1.marks)  # karan 88

s2 = Student("Arjun",69)
print(s2.name,s2.marks) # arjun 69

print(Student. college_name) # ABC college
print(s1.name) #karan


class Student :
        college_name = "ABC college"
        name = "anomynous"  #class attr

        def __init__(self,name,marks):
             self.name = name  #obj attr > class attr
             self.marks = marks

        def welcome (self):
             print("welcome Student",self.name) #output = welcome karan

        def get_marks(self):
              return self.marks


s1 = Student("karan",88)
s1. welcome ()  
print(s1.get_marks())  #output = 88

#create student class that takes name and marks of 3 subject as a argument in conductor . then create a method to print the average .
class Student:
      def __init__ (self,name,marks):
            self.name = name
            self.marks = marks

      def get_avg(self):
            sum = 0
            for value in self.marks:
                  sum+= value
                  print("hi" , self.name ,"your avg score is :",sum/3)

s1 = Student("tony stark",[99 , 98 , 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()  # output = hi ironman your avg score id 98.0

   

class Student:
      def __init__ (self,name,marks):
            self.name = name
            self.marks = marks

      @staticmethod
      def hello( ):
         print("hello")
s1 =Student("megha",[99,98,97])
s1.hello()  # output = hello

class Car:  #abstraction
      def __init__(self):
            self.acc = False
            self.brk = False
            self.clutch = False
      def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()  #output car started..

#encapsulation wrapping data and function inta a single unit (object)

#create account with 2 attribute - balance and account no. create method for debit , credit and printing the balance

class Account:
      def __init__(self ,balance,acc):
            self.balance = balance
            self.account_no = acc

#debbit method
def debit(self,amount):
      self.balance = -amount
      print("Rs.",amount, "was debited")      
      print("total balance =", self.get_balance())     

def credit(self,amount):
      self.balance += amount
      print("Rs.",amount, "was credited")      
      print("total balance =", self.get_balance())    

def get_balance(self):
      return self.balance



acc1= Account(10000,12345)



print(acc1.balance)
print(acc1.account_no)


class Student:         #deleate
      def __init__(self , name):
            self.name = name

s1 = Student("shradha")
print(s1.name)
del s1
#rint(s1.name)

class Person:
      __name = "anomynous"
      def __hello(self):
            print("hello person")

      def welcome (self):
           self.__hello()

p1 = Person()
print(p1.welcome())

#single inheritance

class Car:       
      color = "black"
      @staticmethod
      def start():
            print("car started..")

      @staticmethod
      def stop ():
            print("car stopped.")


class toyotaCar(Car):
      def __init__(self,name):
            self.name = name

car1 = toyotaCar("fortuner")
car2 = toyotaCar("prius")

print(car1.start())
print(car1.color)

#multi level inheritance

class Car:       
      @staticmethod
      def start():
            print("car started..")

      @staticmethod
      def stop ():
            print("car stopped.")


class toyotaCar(Car):
      def __init__(self,brand):
            self.brand = brand

class Fortuner(toyotaCar):
      def __init___(self , type):
            self.type = type

car1 = Fortuner("diesel")
car1.start()

#multiple inheritance

class A:
      varA = "welcome to class A"

class B:
      varB = "welcome to class B"

class C(A,B) :  #c is chilad class so it has to inherited (A,b)
      varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


