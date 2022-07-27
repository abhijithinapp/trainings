""" 
#Exercise
message = "Hello World!"
print(message)


x = x + 2
w += 2
y = y - 2
z -= 2



a = 20
b = 25

print(a)
#del a, b
print (a)

int_eg = 10
float_eg = 100.05

print(int(float_eg))
print(float(int_eg))
print(str(int_eg))
print(str(float_eg))

h = 'I informed that, "Python is easy to learn" '
print(h)

name = 'aju' 
print(name.title())
print(name.upper())
print(name.lower())

f_name = 'aju'
l_name = 'aji'
my_name = f"{f_name} {l_name}"
print(my_name) #aju aji
print(f"Hello, {my_name.title()}!") #Hello, Aju Aji!

make = 'Dell'
dollarrate = 70.6
myText = ' the amount for %s is %d usd and exchange rate is %f.2f usd to 1 inr' %(make, 1299, dollarrate)
print(myText) # the amount for Dell is 1299 usd and exchange rate is 70.600000.2f usd to 1 inr

myText2 = 'the amount for {} is {} usd and exchange rate is {} usd to 1 inr'.format(make, 1299, dollarrate)
print(myText2)  #the amount for Dell is 1299 usd and exchange rate is 70.6 usd to 1 inr

myText3 = '{0} is easier than {1}'.format('Python', 'Java')
print(myText3) #Python is easier than Java
myText3 = '{1} is easier than {0}'.format('Python', 'Java')
print(myText3) #Java is easier than Python

#count()
print('Hello Good Mornuing'.count('d'))
#formatiing
name = "India"
text = "{} is my country. All {}ns are my brothers and sisters.".format(name, name)

print(text)
#India is my country. All Indians are my brothers and sisters.


#endswith()
num = text.count('India')
print(num) #2

myString = " superman"

print(myString.endswith('man')) #True
print(myString.endswith('man', 3)) #True
print(myString.endswith('man', 2, 6)) #False
print("postman".endswith(('man','ma'),2,6)) #True


#find() & index()

myString2 = "Hello Good Morning"
print(myString2.find('Go')) #6
print(myString2.find('Go', 4)) #6
print(myString2.find('Go',4, 15)) #6
print(myString2.find('kk')) #-1
#print(myString2.index('kk')) #ValueError: substring not found

#isalnum()

print('Hello123'.isalnum()) #True
print('H e l l o 1 2 3'.isalnum()) #False
print('Hello'.isalnum()) 

#isalpha()

#isdigit()

#islower()
#isupper()
#istitle()

#join() method used to join in a tuple with a seperator
Seperator = '*'
myTuple = ('h','e','l','l','o')
myNewString = Seperator.join(myTuple)
print(myNewString) #h*e*l*l*o
print(myNewString.lower())
print(myNewString.upper())

#replace()
print('Hello world'.replace('o', 'i')) #Helli wirld
myStr = 'Helo world'
print(myStr.replace('o', 'i', 2)) #Heli wirld
print('Hello world'.split(' ')) #['Hello', 'world']
print(myStr.split(' ')) #['Helo', 'world']


#python REGEX
#refer for more : https://www.w3schools.com/python/gloss_python_regex.asp
# https://www.programiz.com/python-programming/regex
import re
 

txt = "bits of paper bits"
print(txt.find('of')) #5
x =re.findall("bi", txt)
print(x)

#['bi', 'bi']

y = re.search("bi", txt)
print(y)
#<re.Match object; span=(0, 2), match='bi'>

#print(x.span())
#print(x.string)
#print(x.group())
#------------------------------------------------------------------------#
w = re.split(" ", txt)
print(w) #['bits', 'of', 'paper', 'bits']

u = re.split(" ", txt, 1)
print(u) #['bits', 'of paper bits']

t = re.sub(" ", "-", txt)
print(t) #bits-of-paper-bits

txt2 = "hello world"
p = re.findall("[a-m]", txt2)
print(p) #['h', 'e', 'l', 'l', 'l', 'd']

txt3 = "James bond is 007"
q = re.findall("\d", txt3)
print(q) #['0', '0', '7']

r =  re.findall("he..o", txt2)
print(r) #['hello']
#------------------------------------------------------------------------#
#begin search
#metacharacter ^
s =  re.findall("^hell", txt2)
print(s) #['hell']
#these  will check for the pattern

#special sequence \A
o =  re.findall("\Ahell", txt2)
print(o) #['hell']
txt4 = "Watt invented James theso engine"
s1 =  re.findall("\AJam", txt4)
print(s1) #[]
#these  will check for the  pattern

#end search
#metacharacter $
v =  re.findall("world$", txt2)
print(v) #['world']

#special sequence \b at the beginning, end and middle of word
s2 =  re.findall(r"\bworld", txt2)
print(s2)  #['world']

s3 =  re.findall(r"\bthe", txt4)
print(s3) #['the']
#------------------------------------------------------------------------#
#mathcing sn email within a string using special sequences
txt5 = "hello text@gmail.com how are you?"
#regular expression to match email
#check for non space chars before and after '@' , for that use \S
regex = r'\S+@\S+'
s4 =  re.findall(regex, txt5)
print(s4) #['text@gmail.com']

regex1 = r'\S+@\S'
s5 =  re.findall(regex1, txt5)
print(s5) #['text@g']
#------------------------------------------------------------------------#
#Python Lists and List Access Options

from xml.dom.pulldom import START_DOCUMENT


studAge = [18, 21, 23, 20, 21]
#non-destructive nature
print(studAge) #[18, 21, 23, 20, 21]
print(studAge[0]) #18
print(studAge[-1]) #21
print(studAge[2:4]) #[23, 20]
print(studAge[1:5:2]) #[21, 20]
print(studAge[:4]) #[18, 21, 23, 20]
print(studAge[::-1]) #[21, 20, 23, 21, 18]

#destructive nature
#append to add a value to the en of the list
studAge.append(20)
studAge.append("hi")
print(studAge) #[18, 21, 23, 20, 21, 20, 'hi']

#delete a value from the specified location
del studAge[-1]
print(studAge) #[18, 21, 23, 20, 21, 20]

#extend(), in, insert(), len()

#extend(): combine two lists
mylist1 = ['Anu', 'binu', 'Rinu']
studAge.extend(mylist1)
print(studAge) #[18, 21, 23, 20, 21, 20, 'Anu', 'binu', 'Rinu']

#in : to check if a variable is in the list 
#operator
print('Anu' in mylist1) #True
print('Anu' not in mylist1) #False
print('Anus' in mylist1) #False

#len(): to get the number of items in the list
print(len(studAge)) #9

#destructive nature
#reverse() list : it can permanently change the actual list 
print(studAge) 
studAge.reverse()
print(studAge)  #['Rinu', 'binu', 'Anu', 20, 21, 20, 23, 21, 18]

#sort the list alphabetically or numerically
newstudAge = [18, 21, 23, 20, 21]
newstudAge.sort()
print(newstudAge) #[18, 20, 21, 21, 23]
newstudName= ['hina', 'leya', 'aju', 'diya']
newstudName.sort()
print(newstudName) #['aju', 'diya', 'hina', 'leya']

#list concatenation using + operator
print(newstudName + newstudName) #['aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya']

#list dupliaction/multiplication using * operator
print(newstudName*3) #['aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya', 'aju', 'diya', 'hina', 'leya']  


#Tuples in Python

months = ("Jan","Feb","Mar")
print(months[0]) #Jan
print(months[-1]) #Mar
#months[0] = "test" 
# #TypeError: 'tuple' object does not support item assignment
print(len(months)) #3
print("Jan" in months) #True
print("Jan" not in months) #False

#del months
#print(months) 
# #NameError: name 'months' is not defined. Did you mean: 'month'?


print(months + months) #('Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar')
print(months * 3) #('Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar')



#dictionary in Python
#declaration 
#method 1
myStud = {"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"}
print(myStud) #{'Abhi': 30, 'Sibi': 34, 'subi': 'Not available'}

#method 2
mystud2 = dict(Abhi = 28, Sibi = 30, subi = " Not avaialable")
print(mystud2) 

#method 3
mystud3 = dict({"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"})
print(mystud3) 

print(mystud3["Sibi"])
print(myStud)

#dictionary methods
#get()
print(myStud.get("Abhi")) #30
#items()
print(myStud.items()) #dict_items([('Abhi', 30), ('Sibi', 34), ('subi', 'Not available')])
#keys()
print(myStud.keys()) #dict_keys(['Abhi', 'Sibi', 'subi'])
#values()
print(myStud.values()) #dict_values([30, 34, 'Not available'])
#update()
day1 = {1: 'monday', 2:'tuesday'}
day2 = {1:'wednesday', 2:'thursday'}
day1.update(day2)
print(day1) #{1: 'wednesday', 2: 'thursday'}
#len()
print(len(day1))
#in operator
print("abhi" in myStud) #False
print(30 in myStud.values()) #True

#clear() : to delete al the items and return an empty set
day1.clear()
print(day1) #{}

#del : delete the entire dictionary
del day2
print(day2) #NameError: name 'day2' is not defined. Did you mean: 'day1'?

#dictionary in Python
#declaration 
#method 1
myStud = {"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"}
print(myStud) #{'Abhi': 30, 'Sibi': 34, 'subi': 'Not available'}

#method 2
mystud2 = dict(Abhi = 28, Sibi = 30, subi = " Not avaialable")
print(mystud2) 

#method 3
mystud3 = dict({"Abhi" : 30, "Sibi" : 34, "subi" : "Not available"})
print(mystud3) 

print(mystud3["Sibi"])
print(myStud)

#dictionary methods
#get()
print(myStud.get("Abhi")) #30
#items()
print(myStud.items()) #dict_items([('Abhi', 30), ('Sibi', 34), ('subi', 'Not available')])
#keys()
print(myStud.keys()) #dict_keys(['Abhi', 'Sibi', 'subi'])
#values()
print(myStud.values()) #dict_values([30, 34, 'Not available'])
#update()
day1 = {1: 'monday', 2:'tuesday'}
day2 = {1:'wednesday', 2:'thursday'}
day1.update(day2)
print(day1) #{1: 'wednesday', 2: 'thursday'}
#len()
print(len(day1))
#in operator
print("abhi" in myStud) #False
print(30 in myStud.values()) #True

#clear() : to delete al the items and return an empty set
day1.clear()
print(day1) #{}

#del : delete the entire dictionary
del day2
print(day2) #NameError: name 'day2' is not defined. Did you mean: 'day1'?

#Python Sets
#unordered collection, some memory can be saved 
#no index, so we can't access them directly
#create using set() or {}


#method 1
months = {"January", "February", "March", "April"}
print(months) #{'January', 'February', 'April', 'March'}
print(type(months)) #<class 'set'>

#method2
mon = set(["jan","feb","mar"])
print(mon) #{'feb', 'jan', 'mar'}

#declare an empty set
day = set()
#add values one by one only
day.add("monday")
day.add("tuesday")
day.add("wednesday")
print(day) #{'monday', 'wednesday', 'tuesday'}


#day.add(["thursday", "friday"])
#print(day) #TypeError: unhashable type: 'list'

#to add multiple items
day.update(["thursday", "friday"]) 
print(day)
#{'friday', 'monday', 'tuesday', 'thursday', 'wednesday'}


print("the set selements are:")
for i in months:
    print(i)
    #(the set selements are:
    # January
    # February
    # April
    # March)


#remove items
#discard() : remove item and donot display error if not exists
day.discard("thursday")
print(day) #{'tuesday', 'wednesday', 'friday', 'monday'}

#remove() : remove item and will display error if not exists
#day.remove("thursday")
#print(day) #KeyError: 'thursday'

#loop through 
for days in day:
    print(days)
    #(friday
    # monday
    # wednesday
    # tuesday)

#clear the elements in the set
day.clear()
print(day) #set() : empty set is displayed


#SET operations
#union() :  exclude duplicates but combine both sets
#calculated using pipe(|) operator or union() function
#if two pipes (||) caleed as pipeline
m1 = {"Jan","Feb","Mar"}
m2 = set(["Mar","Apr","May"])

m3 = m1 | m2
print(m3) #{'Feb', 'Apr', 'Jan', 'May', 'Mar'}

for m in m3:
    print(m)

#intersection() 
#using & operator or the intersection() function
m4 = m1 & m2
print(m4) #{'Mar'}

m5 = m1.intersection(m2)
print(m5) #{'Mar'}

#intersect_update()
#will remove values that are not in other sets
a = {"tom", "jerry", "mickey"}
b = {"jerry", "tom", "donald"}
c = {"winne", "mickey", "tom"}
a.intersection_update(b,c)
print(a) #{'tom'}

#difference()
#using - operator or difference() method
m6 = m1 - m2
print(m6) #{'Jan', 'Feb'}
m7 = m2 - m1
print(m7) #{'May', 'Apr'}

#symmetric diffrence: remove elements in both sets 
#calculated by ^ operator or symmetric_difference() method
m8 = m1 ^ m2
print(m8) #{'Feb', 'Jan', 'May', 'Apr'}

#calculated by ^ operator or symmetric_difference() method
m9 = m1.symmetric_difference(m2)
print(m9)

#symmetric_difference_update()
months1 = {"Jan", "Feb", "Mar"}
months2 = {"Mar", "Apr", "May"}
months3 = {"Feb", "Mar", "Jun", "jul"}

#Set comparison Operators 
#Checking if months1 is superset of months2
print(months1>months2)
print(months1<months2)

#Check if two sets are equal
print(months2 == months3)

# Check if two sets are equal as well as month1 is a superset of month2
print(months1 >= months2)

#Frozen set
months4frozen = frozenset([{"nov", "dec"}]) #immutable set 
print(months4frozen)
print(type(months4frozen))
months4frozen.add("oct") # frozenset object has no attribute 'add'


#input and output functions in python 
studentName= input("Please enter your name:")
print(studentName)
studentAge = input("Please Enter your age: ")

#variations of print statement to include variables
print("The student name is", studentName, "and the age is ", )
print("The student name is %s and the age is %s" %(studentName, studentAge))
print("The student name is {} and the age is {}".format(studentName,studentAge))

# To print in multiple lines 
print('''Hello World
How are you''')

# To print a new line 
print('Hello \n world')
print('This is a backlash \\')
print('I am 5\' 5\" tall')

#Control Flow statements
#Conditional statements 
#If condition

userInputNo = input("Enter either 1 or 2: ")
if(userInputNo == "1"):
    print("You entered 1")
    print("And you are the no 1")
elif(userInputNo == "2"):
    print("You entered 2")
    print("Runner up. Keep it up!")

#Inline If Statement
B = 12 
A= 12 if B == 12 else 13
print(A)

# Python match case statement example
#define a function
def http_status(status):
    match status: 
        case 400:
            return "Bad request"
        case 404: 
            return "Page not found"
        case _:
            return "unknown error occured"
print(http_status(404))

#try and except
try:
    print(5/0)
except:
    print('error')

#functions
def checkIfPrime(numberToCheck):
    for x in range(2,numberToCheck):
        if(numberToCheck%x==0):
            return False
    return True

print(checkIfPrime(5))

#function returning multiple values 
def calculations(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a % b
    return (add, sub, mul, div)

#calling the functions
output = calculations(40,30)
print("Sum is ", output[0])
#Generator is a function that returns an iterator 
#iterator is something that we can loop through using a looping statement
from email import message
from tkinter import Y


def calculationsyield(a,b):
    add = a+b
    yield add
    sub = a-b
    yield sub
    mul = a*b
    yield mul

#using a for loop we can loop through the returned value from the function
for value in calculationsyield(30,40):
    print(value)

message1 = "just a global variable"
def myFuction ():
    print("reached inside function ")
    print(message1)
    message2 = "Its a local variable" # declaring a local variable
    print(message2)
    message1  = "This is a modified variable"
    print(message1) #printing the global variable


#lambda functions in python
sum = lambda num1, num2: num1+num2

#calling the lambda function 
print("Sum of two numbers: ", sum(2,3))

#Python Modules
#importing a module


import random
#calling function inside the module 
print(random.randrange(1,10))

import random as r 
#calling function inside the module 
print(r.randrange(1,10))

#importing only specific function from the module 
from random import randrange, randint
print(randrange(1,10))

#python date time module 
import time
print(time.time()) #seconds past 1st jan 1970
print(time.localtime(time.time())) #get the multiple time values as a tuple
print(time.asctime(time.localtime(time.time())))

for i in range(0,10):
    print(i)
    time.sleep(1) # delay the program execution by the specified number of seconds.

import datetime
print(datetime.datetime.now()) #return the current date time object

#creating custom datetime object
birthDay = datetime.datetime(2022, 7, 20)
print(birthDay)
birthDay = datetime.datetime(2022,7,20,10,15,50)

from datetime import datetime as dt
if dt(dt.now().year,dt.now().month, dt.now().day,9)

#python calender module
import calendar
myCalendar = calendar.month(2022, 7 )
#print(myCalendar)
myCalendar = calendar.prcal(2022)
print(myCalendar)

#python math module 
import math
number = 2e-7 #small value of x
print(math.log(math.fabs(number),10))

number = math.pow(4,2) #4 to the power of 2 
print(number)
number = math.floor(4.3) #will round to the smallest digit
print(number)
number = math.ceil(4,3) #will round to the next digit
print(number)
number = math.fabs(-10) #will return the factorial
print(number)
number = math.factorial(10) #will return the factorial
print(number)
number = math.modf(3.14) #will return the int and factorial part
print(number)


#calling the custom module created 
import prime
answer = prime.checkIfPrime(13)
print(answer)

#rights of a fuction in python 
#is similar to the rights of a variable 
#1 we can assign a function to a variable 

def myfuc1():
    print("This is myfunc1")

#5. The inner funtion can access the enclosing function variables 
def myOuter(myGreeting):
    print("The outer function says ", myGreeting)

    def myFirstInnerFunc():
        print("The first inner func says ", myGreetin)
    
    return myFirstInnerFunc

myOuterFuncVariable = myOuter("Peace to the world")
myOuterFuncVariable()


#Python decorator - a function, which accepts another function, enhance it with a wrapper function , enhance it with a wrapper function and return the enhanced function back
# define a wapper function and return the enhaced function back 
# 
# define the decorator function, which accepts another function as the arguments   
def myDecorator(myFunc):
    def innerWrapper():
        print("Before the Function Call")
        myFunc()
        print("After the Function Call")
    return innerWrapper

#defining a simple fn to pass into the decorator 
def myFnToPassIntoDecorator():
    print("A simple fumction to pass into decorator")

myDecoratorDemo = myDecorator(myFnToPassIntoDecorator)

#execute the decorator 
myDecoratorDemo()

#defining another simple function to pass into the decorator 
@myDecorator
def newmyFnToPassIntoDecorator():
    print("A new simple function to pass into decorator")
newmyFnToPassIntoDecorator()

#Main concepts of Object-Oriented Programming 

#Define a simple class with a constructor that can accept two variables
class Employee:
    empCount = 0
    
    #defining a constructor
    #that can accept two values name and salary 
    #save those values into self (self is an instace of the class)
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1 #increment the employee count when a new obj is created

    #define one more simple member function
    def displayEmpCount(self):
        print("Total number of employees:", Employee.empCount)

    #define one more simple member function
    def displayEmployeeDetails(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

#create an object of employee class
employee1 = Employee("Tom", 2000)
employee1.displayEmpCount()
employee1.displayEmployeeDetails()
employee2 = Employee("Jerry", 3000)
employee2.displayEmpCount()
employee2.displayEmployeeDetails()
#accessing the variable directly from the class w/o object (not recommended)


#inheritance

#Demonstrating the base class
#Defining the Base class
class Rocket:
    #definign the constructor
    def __init__(self,name, distance):
        self.name = name
        self.distance = distance

    #defining a member function which returns a string
    def launch(self):
        return "{} has reached {}". format(self.name,self.distance)

class MarsRover(Rocket) :
    def __init__(self, name,distance, maker, vehicleCode):
        Rocket.__init__(self,name,distance)
        self.maker = maker
        self.__vehiclecode = vehicleCode
    def printMaker(self):
        return "%s launched by %s" %(self.name, self.maker)
    def getVehiclecode(self):
        return self.__vehiclecode
    
class plutoRover(MarsRover):
    def getVehicleCodefromMarsRover(self):
        return "%s has reached %s" %(self.name, self.distance)
        
#Create object (instance) for main class Rocket
x = Rocket("Small rocket", "till stratosphere")
y = MarsRover("mars rover", "till mars","ISRO","33")

print(x.launch())
print(y.launch())
print(y.printMaker())
print(y.getVehiclecode())

#Decorating methods of a class

class Hero:
    @classmethod
    def say_class_hello(cls): #since its classmethiod, will receive class rewf as implicit 
        if(cls.__name__ == "HeroSon"):
            print("Hi Prince, called from HeroSon")
        elif(cls.__name__ == "HeroDaughter"):
            print("Hi Pricess, called from HeroDaughter")
    
    #define the decorator @staticmethod
    @staticmethod
    def say_hello():
        print("Hello...") 
    
class HeroSon(Hero):
    def say_son_hello(self): #first implicit arg will be self since its a regular method
        print("Hello son from sub class HeroSon")

class HeroDaughter(Hero):
    def say_son_hello(self):
        print("Hello daughter from sub ")

testHeroSon = HeroSon()
testHeroSon.say_class_hello()

testHeroDaughter = HeroDaughter()
testHeroDaughter.say_class_hello()

class House:
    def __init__(self, price):
        self.__price = price
    
    #creating a getter method for fetching the attribute value in a class
    @property
    def price(self):
        return self.__price

    #creating a setter method decorator
    @price.setter 
    def price(self, new_price):
        self.__price = new_price
    
    @price.deleter
    def price(self):
        del self.__price

#typical access and update will be like this:
house = House(500000) #create obj
print(house.price) #access attributes
house.price = 1000000 #modifying the attribute
print(house.price) #access attribute
del house.price #delete attribute
print(house.price) #ace
#File handiling Demo using Python
#trying to open a file myfile.txt in the same dir
#using open() method get the file object
myFile = open("myFile.txt", "r")
print(myFile.read())
myFile.readline()

#A simple example for higher order function 
#which can accept at least one fn and can optionally return a fn

# a simple fn with a print statement
def greet(name):
    return "Hello {}".format(name)

#define the higher order fn which can accept fn
def print_greetings(fn,param):
    print(fn(param))

#calling the higher order fn
print_greetings(greet,'Abhi')

#using the map function
def mymapfunction(a):
    return a * a

x = map(mymapfunction,[1,2,3,4])
print(list(x))

#map() fn - a higher order fn which can accept a fn and also 
#a list of iterable params. Each param will be applied to the fn
#result will be returned back as a map obj
#we can later convert this map obj into set/tuple

#defining a simple fn
def mymapfunction(a):
    return a * a

#calling the map fn, passing the fn as well as the iterables
x = map(mymapfunction, (1,2,3,4))
#x is a map obj, need to convert that into a set/tuple
print(tuple(x))

#passing a lambda fn as well as teh iterables
x = map(lambda x: x *x, (1,2,3,4))
#x is a map obj, need to convert that into a set/tuple
print(tuple(x))

#filter function which filters the iterables basef on condition 
#it accepts the fn and also the iterables as parameters

#defining a filter condition function
def filterfn(x):
    if x>=3:
        return x

#calling the filter fn passing the condition fn and iterables 
y = filter (filterfn,(1,2,3,4))

#converting the returned filter obj into tuple/list/set etc
print(list(y))

#calling the filter function using lambda funnction
y = filter(lambda x:(x>=3), (1,2,3,4))

#converting the returned filter obj into tuple/list/set etc
print(list(y))

#reduce fn to reduce the list of values based on the operation we 
#it will accept the fn (preferably lambda) and the iterables

from functools import reduce
x = reduce(lambda a, b: a+b, [23,21,45,98])
print(x)       


#class and regular functions without the abstract class
from abc import abstractmethod


class Lion:
    def give_food(self):
        print("Feeding a lion with raw meat")

class Panda:
    def feed_animal(self):
        print("Feeding a panda with bamboo")

class Snake:
    def feed_snake(self):
        print("Feeding a snake with mice")

#Animals we plan to food:
simba = Lion()
kunfupanda = Panda()
kingcobra = Snake()
simba.give_food()
kunfupanda.feed_animal()
kingcobra.feed_snake()

from abc import ABC, abstractmethod
from ast import Param
class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass # just a placeholder function to escape empty fn error
    @abstractmethod
    def do(self,action):
        pass
class Lion(Animal):
    def feed(self): #must implement feed because its abs method
        print("Feeding a lion with raw meat")
    def do(self, action):
        print("Lion is good at {}".format(action))
class Snake(Animal):
    def feed(self):
        print("Feeding a snake with mice")
    def do(self, action):
        print("Snake is good at {}".format(action))

class Panda(Animal):
    def feed(self):
        print("Feeding a panda with bamboo")
def do(self, action):
        print("Panda is good at {}".format(action))

zoo = [Lion(), Panda(), Snake()]
#instead of calling method repeatedly like the above,
#we can have a for loop for the list of classes
for animal in zoo:
    animal.feed()

#To print lines in file
myFile = open("myFile.txt", "r")
for line in myFile:
    print(line)
myFile.close()

myFile = open("myFile.txt", "r")
#read all the lines and return it as a  list
myFileContentList = myFile.readlines()
print(myFileContentList)
myFile.close()

#opening the file cursor in append mode
#whatever content we write will be appended to the end of file
myFile = open("myfile.txt", "a")
#write() method is used
myFile.write("Humpty Dumpty sat on a wall\n")
myFile.close()

#renaming a file using python os module
import os
if os.path.exists("myFile.txt"):
    os.rename("myFile.txt", "myFileNew.txt")
    print("rename success")
else:
    print("file doesnot exist")

#create a new directory

import os
print(os.getcwd())
os.chdir("mydir")
print(os.getcwd())

import subprocess
with open("myFile.t")


#A simple demonstration of Exceptiion handling in python 
#using the try, except, finally blocks (clause)

try:
    div = 4//0
    print(div)

except ZeroDivisionError:
    print("You are trying to divide a number by 0")

except Exe:
    print("Sorry some error occured")

finally:
    print("It will run whatever happens")


try:
    div = 4//2
except Exception as e:
    print("You are trying to divide a number by 0")
    print(f"{type(e).__name__} was occured. More details below:")
    print(e)
else: #else will work if try statement is successfull
    print(f"division completed and result is {div}")

finally:
    print("It will run whatever happens")

#Nested try except statements in python: a scenario
try:
    f = open("somefile.txt")
    try: 
        f.write("Hello world")
    except:
        print("Some write error occured")
except:
    print("the file cannot be opened")

x = "Hello World"
if not type(x) is int:
    raise TypeError("Only numbers are allowed")
x=0
if x == 0:
    raise Exception("The number cannnot be zero")
"""

#creating a user defined Exception class
#Exceptions should be derived from the built-in exception class

#creating a class inheriting the builtin Exception class
from re import S


class myError(Exception):
    #creating the constructor
    def __init__(self,value):
        self.value = value
    #the __str__ dunder method
    def __str__(self):
        return(repr(self.value))

#__str__ magic fn is used to get the informal string that 
#represent the obj

#using the class that we just created
try:
    x = 0 
    if x==0:
        raise(myError("Number cannot be zero"))
except myError as error:
    print('A new Exception occured', error)

#using the class that we just created 

#the exception derived class being inherited by another class
class myError(Exception):
    #base class for exceptions
    pass
class DivideByZero(myError):
    pass

try:
    x = 0
    if x == 0:
        raise DivideByZero
except DivideByZero:
    print('A new exception occured ')
    print("hello")

#creating a class with an empty list of software names 
#and an empty dict of software name and version as key value pairs 
class Softwares:
    name = []
    versions = {}

    #defining the constructor 
    def __init__(self,names):
        if names:
            self.names = names.copy() #create a copy of the list
            for name in names: # looping through the list
                self.versions[name] = 1
                #initialize sw version to 1 for all sw names
        else:
            raise Exception("Names cannot be empty")
            
    #overriding the str dunder for displaying the list of sws
    def __str__(self):
        s = "The list of s/ws and its versions are: \n"
        for key, value in self.versions.items():
            s += f"{key}:{value} \n"
        return s

        #loop through the dict and print the list
        
