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
"""
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

