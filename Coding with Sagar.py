'''a =input("Enter first number:")
b= input("Enter second number:")
c =input("Enter the operation out of +,-,*,/:")
try:
    a=int(a)
    print("a is an integer")
except:
    try:
        a=float(a)
        print("a is float")

    except:
        print("int ya float mein baat kar!")
        exit()

try:
    b=int(b)
    print("b is an integer")

except:
    try:
        b=float(b)
        print("b is float")
    except:
        print("int ya float mein baat kar!")
        exit()

try:
    c=str(+) || str(-) || str(*) || str(/)
    print("Right expression")

try:
    expression = str(a)+c+str(b)
    result = eval(expression)
    print(result)'''

'''my_list = ['mango','apple','banana']
my_tuple = ('mango','apple','banana')

#Lists are mutable but tuples and strings are immutable
#Set is unordered collection of unique items

set = {1,1,1,2,3,4,5}
print(set)

#above is a set which is mutable, below is a frozen set that is immutable
immutable_set = frozenset([1,1,1,2,3,4,5])
print(immutable_set)'''


'''num_1 = float(input("Enter number 1:"))
num_2 = float(input("Enter number 2:"))
choice = input("Enter your choice + - /:")

if choice == '+':
    print(f'Addition: {num_1 + num_2}')

elif choice == '-':
    print(f'Subtraction:')
    if num_1>num_2:
        print(f'Greater minus smaller: {num_1 - num_2}')
    elif num_2>num_1:
        print(f'Greater minus smaller: {num_2 - num_1}')
    else:
        print("Barabar matlab 0")

elif choice == '/':
    print("Division:")

    if num_2 == 0:
        print("I na cholbe")

    else:
        print(f'Division: {num_1/num_2}')'''


'''a= list(range(1,10,1))      #range function
print(a)

b = tuple(range(1,10))       #by default difference 1 ka hi hota hai
print(b)
'''

'''for num in range (1,10):
    if num == 5:
        break
    print(num)'''


'''for num in range (1,10):
    if num == 5:   
        continue  #Bs 5 skip hua aur 1 se 9 sab chala
    print(num)'''

'''start = int(input("Enter start of the series:"))
stop = int(input("Enter ending number of the series:"))
skip = int(input("What number you hate in this range?"))
for i in range (start,stop+1):
    if i == skip:
        continue
    print(i)'''

#There maybe many different conditions for such control statements. Try different combinations in your experiment file.

'''a = "python"
for i in a:
    print(i)'''
#len function
#Slicing [start:stop:step]

'''a = "Python is my first language"
print(a[0:13:2])     #13 exclusive
print(a[13])
print(a[1:13])       #13 exclusive
print(a[::-1])'''

'''a = "Python is my first language"
print(a.find("y"))        #Case sensitive and tells first occurence
print(a.replace("Python", "Javascript"))'''

#splitting and joining methods

'''str = "1,2,3"
s = str.split(",")
print("After splitting: ",s)

a = (",").join(s)
print("rejoining: ",a)'''

#boolean = startswith, endswith, isalpha, isdigit, isalnum

#methods of creating a list:

'''a = list(("Dev", 1, 1.2, True))
print(a)

lst = ["Dev", 1, 1.2, True]
print(lst)'''

'''lst = ["Dev", 1, 1.2, True]
lst[0:3] = "Shree", 2, 2.2
print(lst)'''

#Concatenation

'''lst_1 = ["Shree",1,2,3,4,True]
lst_2 = ["Dev",6,7,8,9,False]
print(lst_1+lst_2)          #ek hi list mein sath aayenge
print(lst_1 *3 + lst_2 *2)    #Again rhegi ek hi list'''

'''a = [1,2,3,4,5,6]
enter = int(input("Enter an integer:"))
if enter in a:
    print("Found")

else:
    print("Naah")'''

#Alias and Cloning
#Alias, again equal to krne se do variables ek data ko point out kr rhe hain

'''a = [1,2,3]
b = a
b[0] = 8
print(a)       #Changed a

c = a.copy()
c[0] = 1
print(c)
print(a)'''

#Methods
'''a = [1,2,3]
a.append(4)    #ending mein hi add
print(a)
b = [5,6,7]
a.extend(b)
print(a)'''

#instert(index, value)

'''a = [0,1,2,3]
a.insert(2, "Hello Dv!")
print(a)       #it won't replace, just insert
a.remove(3)
print(a)'''

#pop(index)
'''a = [1,2,3,4]
print(a.pop(0))    #jinko udaya hai
print(a)         #udane ke baad mein jo bacha hai
a.clear()
print(a)'''

#index(element)       to know the index of the element
'''a = [1,2,3,4,5,4,5,6,1,2,3]
print(a.index(4))
print(a.count(4))'''

'''a = [3,2,1,-8,8,4,3,2]
print(a.sort())    #Dono kaam sath mein krne gye to none hi return hoga
a.sort()     #pehle procedure pass krna hai
print(a)     #phir print krna hai

a.reverse()
print(a)'''

#min and max
'''a = [1,2,4,0,6,8,3,6,9,6,6]
print(min(a))
print(max(a))
for i in a:
    if a.count(i)>1:
        print(i)''' #repeat wala object jitni baar hai utni baar print hoga

#Common elements between two lists - Use sets
'''a = [1,2,3]
b = [3,4,5]
sa = set(a)
sb = set(b)
si = sa.intersection(sb)
print(f'{si}')
print(list(si))'''

#Nested List
'''a = [1,2]
b = [1,2,a,3,4,5]
print(b) '''  #is time list a ko pura show krega

#range function

'''a = range(1,11,1)
print(a)
print(list(a))'''

#Comprehension
'''b=[]
for i in range (1,11):
    a = i**2
    print(a)
    b.append(a)
print(list(b))'''

#Better way [expression for item in iterable if condition]

'''a = [i**2 for i in range(1,11) if i%2 == 0]
#bani banai list bhi dedi bracket se
print(a)'''

#Tuples
'''a = (1,2,3,4,5,6)
#slicing, len, max, min possible - anything which doesn't change the original data
print(a[0:4:2])
print(max(a))
print(min(a))
print(len(a))'''

#Dictionaries
#Data in the form of related pairs (key and value pairs)

#Value can be anything - another dict, string, list, tuple.
#And Key should always be unique

'''my_dict = {"name":"Devshree", "age":21, "language":"Python"}
print(my_dict)
print(type(my_dict))'''

#Operations on dictionary:

'''my_dict = {"Fruits":["Apple","Banana", "Mango"], "Category":"Fruit"}
print(my_dict)
my_dict["Price"]=100   #This way is also used to update an existing key's value
print(my_dict)'''
#mutable

'''my_dict = {"interests": ["networks","animation","mathematics"],
           "branch": "engineering",
           "age":21}'''
'''print(my_dict)
del my_dict["interests"]
print(my_dict)'''

'''my_dict["interests"].remove("mathematics")
print(my_dict)'''

#Methods
#Get
'''age = my_dict.get("age")
print(age)
color = my_dict.get("color", "not found")
print(color)'''
#Keys
'''keys = my_dict.keys()
print(list(keys))
#Values
values = my_dict.values()
print(list(values))'''
#Items
'''all_dict = my_dict.items()
print(list(all_dict))'''
#Pop
'''popped = my_dict.pop("age")  #not found ka msg yahan add ho skta hai
print(popped)
print(my_dict)'''
#Pop Item - Last pair ko uda dega
'''last_pop = my_dict.popitem()
print(last_pop)
print(my_dict)'''
#Clear - Puri dictionary khali krne ke liye
'''cleared = my_dict.clear()  
print(my_dict)'''

#Dictionary Comprehension
'''squares = {x:x*x for x in range(1,6)}
print(squares)'''

'''hehe = {x: 100+x for x in range(1,10) if x%2==0}
print(hehe)'''

#[expression for item in iterable if condition]

#Nested Dictionary
'''daily = {"routine":{"morning":"exercise","evening":"studies","afternoon":"college"},
         "food habits":{"breakfast":"milk","lunch":"khichdi","dinner":"roti"}}
print(daily)'''

#Loops in dictionary

'''end = {"Name":"Dev","Age":21,"Language":"Python"}
for k in end:   #prints keys by default
    print(k)
for i in end.values():
    print(i)
for r in end.items():
    print(r)'''

#Functions
'''def greet():   #defining function
    print("hello")   #task
greet()   #calling the function'''

#Parameters and arguments
#Parameters are the placeholders (variables) for the values you pass while calling a function
#Arguments - The actual value in the placeholder (parameter)

'''def greet(name):
    print("Hello!",name)
greet("Devshree")
greet("Rahul")
greet("Kapil")'''
#Name is the parameter; Devshree, Rahul and Kapil are the arguments
'''There are three types of arguments:
Positional
Keyword
Default'''

#Positional - Output should be passed in the defined order
'''def greet(name,city):     #defined order
    print(f'Welcome to {city} {name}')
greet("raju", "mumbai")    #output order'''

#Keyword -
'''def greet(name,city):     #defined order
    print(f'Welcome to {city} {name}')
greet(city="mumbai",name="raju")    #I can change the output order after defining'''

#Default -
#Suppose the user passes no argument in the end, so we keep a default argument while making the function with parameter itself
'''def greet(name="raju", city="mumbai"):
    print(f'Welcome to {city} {name}')
greet()   #raju and mumbai dominate
greet(city="kanpur",name="anna")   #anna and kanpur dominate'''

#Return Statement

'''def get_full_name(first, last):
    full_name=f'{first} {last}'  #full_name is an object
    return full_name
#function needs to be stored in a variable while using return
name = get_full_name("Gopal","Sharma")  #ye tabhi chalega jab function kuchh return kr rha hai, iska whi objective hai
print(name)'''

#Print sirf information display krta hai, lekin return ek value bhejta hai caller ko aur phir function ko exit krr deta hai

#Local and Global variables
#Local variables - Function ke andar hi bante hain aur sirf wahin use ho skta hai
#Global variables - Function ke bahar bante hain, sab jagah use hote hain

#Local variables
'''def msg():
    choice = "I love coding wise"
    print(choice)
msg()
print(choice) '''  #This statement is incorrect as choice was a local variable
#Global variables
'''stat = "My name is Devshree Sharma"
def glo_bal():
    print(f'Hello, {stat}')
glo_bal()
print(stat)'''

#Decorators and generators

#Decorators
'''Adding another function inside the main function without 
changing its functionality is called decorator'''

'''def my_dec(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper
@my_dec
def hello():
    print("Hello")
hello()'''
#Original function mein modification kiya bina us function ke code ko chhede

#Generators - to prevent overutilization of memory
'''They generate on demand values'''
'''def count_down(num):
    while num>0:
        yield num   #yield values one at a time
        num-=1
for number in count_down(5):
    print(number)

for i in range(5,0,-1):
    print(i)'''
#The difference is about memory allocation

#Lambda Functions
#Syntax - lambda argument:expression condition

'''squares = lambda x:x*x
print(squares(5))'''

#To make it a bit complicated using chatgpt
'''squares = lambda x:x*x
result = list(map(squares, range(1,11)))
print(result)'''

#Object Oriented Programming

#Object has Data and Methods

'''class Character:
    def __init__(self, name, health, attack):  #Data (Attributes/Properties)
        self.name=name
        self.health=health
        self.attack=attack

    def attack_enemy(self):   #Method
        print(f'{self.name} attacks with power {self.attack}')

warrior = Character('Thor',100,50)    #Objects
mage = Character('Gandalf', 80, 70)
archer = Character('Archer', 40, 20)

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()'''

#Classes and Objects
'''Class is a blueprint or template for creating objects
Class - map
Object - house
Objects are the actual instance of a class (existing physically)'''

'''class Car():
    def start(self):   #Methods - start, stop  
        print("Car is starting....")
    def stop(self):
        print("Car is stopping.....")

car1 = Car()    #Objects
car2 = Car()

car1.start()   #Objects ke sath class ke andar ke methods ko call kra
car1.stop()

car2.start()
car2.stop()'''
#Tip for you - You can understand OOPS comparing them with Functions concepts using ChatGPT
#Is baar Car wale mein hi data bhi dalenge
'''class Car:
    def set_details(self, brand, color):   #Smjh lo ye parameter hain, niche inmein arguments pass honge
        self.brand = brand
        self.color = color

    def show_details(self):    #Method
        print(f'This car is a {self.color} {self.brand}')

car1=Car()  #object banaya car1 naam ka
car2=Car()   #Aur yahan object banaya ek aur car 2 naam ka

car1.set_details("Tesla", "Red")   #Properties wale method ko call krke arguments pass kr rhe hain
car2.set_details("Maruti", "White")

car1.show_details()    #Method ko call kr rhe hain
car2.show_details()'''

#What is self? - Self is a special keyword/variable used inside a class to refer to the current object

'''class Car:
    def set_details(self, brand, color):
        self.brand = brand   #current object ke andar ye property store krr
        self.color = color

        print(brand, color)

car1 = Car()  #Jo methods bataye the aur har current object ko self se represent krk jo bataya tha ye wo ek object hai, ismein bataye hue kaam ko store ya execute krna rhega (property ya method)
car1.set_details("Tesla","Red")'''

#Always use self to store properties inside an object

#Constructor - Basically the automatic default operation
#Without Constructor:
'''class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
car1 = Car()
car1.set_details("Tesla","Red")  #Bina constructor ke set_details method ko manually call krna pada
print(car1.brand)
print(car1.color)'''

#With Constructor:
'''class Car:
    def __init__(self, brand, color):  #Brand aur color parameters hain
        self.brand=brand  #Ye line self ki property (self.brand) ki value store krta hai inside the object (as brand) - niche object banakr program likhte hue khud se wo parameters show krta hai
        self.color=color
#Alag se set_details ko call krne ki koi zarurat nhi padi
car1 = Car("Tesla", "Red")
print(car1.brand)
print(car1.color)'''

'''class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Rakesh",19, "A")
student2 = Student("Dev",20, "B")

print(student1.age)
print(student2.name)'''

#Types of Constructors - Try it
'''Default  (self)
Parameterized  (self, name, age)
Default (self, name = unknown, age = 0'''

#Polymorphism - one name, many forms
#Ek function alag alag datatypes ke liye alag tareekon se kaam kr rha hai

'''print(len("Python"))
print(len((1,2,3)))  #list
print(len([1,2,3]))   #tuple
print(len({"a":1, "b":2, "c":3}))'''

#Polymorphism with classes
'''class Bird():
    def sound(self):
        print("Birds make sounds")

class Crow(Bird):   #Inheritance ka use kiya yaha
    def sound(self):
        print("Crow says caw caw")

class Cukoo(Bird):
    def sound(self):
        print("Cukoo says koo")

bird1 = Crow()   #Creating object
bird2 = Cukoo()

bird1.sound()
bird2.sound()'''

'''Output
Crow says caw caw
Cukoo says koo'''

#Method name same hai pr outputs different hai based on the objects - method ka naam to sound hi tha pr outputs bird1 aur bird2 ke liye different the

#Polymorphism with Operators
#Same functionality ko different tareekon se basically use krna

'''print(10+5)
print("Hello"+"World")
print([1,2]+[3,4])'''

#Encapsulation methods - sensitive data ko hide krk controlled access provide krna
'''class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        #self.balance = balance  #public variable
        self.__balance = balance  #private variable

    def deposit(self, amount):   #Ek method bana rhe
        self.__balance += amount
        print(f'Deposited {amount}. New balance {self.__balance}')

    def get_balance(self):
        return self.__balance       #Controlled access

account = BankAccount(12344, 400)
account.deposit(200)
print(account.get_balance())
print(account.__balance) '''  #Python will give error - cause this property is not available publically

#Inheritance - Parent class mein likhe hue method ya code ko child class mein reuse krna
'''class Animal:
    def speak(self):
        print("Animals make sounds")

class Dog(Animal):   #Jab hm chahte hain ki upar wali class ki property ka use ho
    def bark(self):
        print("Dogs bark")

dog = Dog()
dog.speak()   #speak method ka bhi use krr skte hain dog class ke andar, kyuki animal class ko inherit kiya tha
dog.bark()'''

#Data Abstraction - Hiding complex details and just showing necessary ones

'''from abc import ABC, abstractmethod
class Vehicle(ABC):   #ABC pass krna hoga kyuki us module ki properties hm is class mein inherit kr rhe hain
    @abstractmethod
    def start(self):
        print("Vehicle for roads")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

car=Car()
bike=Bike()

car.start()
bike.start()'''

'''Output
Car starts with a key
Bike starts with a button'''

#Abstraction hide unnecessary details, like here, Vehicle was abstract class so its statement didn't pass
#Abstract classes act as a blueprint, and child classes must define abstract classes

#Exception Handling
'''Errors in Python:
Compile time errors  (execution ke pehle catch hone wali galati, basically syntax errors)
Runtime errors (execute hote hue error aa gaya, jaise kisi int ko zero se divide krna)
Logical errors (program runs without crash but output is not as expected)'''

#Tumhe pata hai ki kahin pr runtime error aayega, pr wo condition code mein rkhna important hai aur code ko crash bhi nhi hone dena hai, is kaam ke liye hai exception handling

'''Here we have try and except blocks
try - wo code likhenge jismein lagta hai ki error aa skta hai
except - wo code likhenge jo batayega ki error aa gaya to bhai kya krna hai'''

'''try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(result)

except ZeroDivisionError:  #ye naam recommended mein hi aa gaya tha
    print("You can't divide 10 from 0")

except ValueError:
    print("Bhai number ko string se divide krega kya")

finally:
    print("Program sampann hua")'''

#So instead of crashing, program prints the statement in except block
#Finally block - Ye hmesha chalega

#Nested try-except block

#Custom Exception - Zabardasti python ka error raise krwakr phir uska statement denge
'''def check_age(age):
    if age<18:
        raise Exception ("Kids not allowed")
    print("Allowed")

try:
    a = int(input("Enter your age: "))
    check_age(a)
except Exception as e:
    print(e)'''

#File Handling
'''2 types of files:
1 - text files (.txt, .csv)
2 - binary files (.png, .jpg, .mp3, .mp4, .pdf)'''
#Opening file - we have function for this - open("file name.txt", "mode")
'''file = open('File.txt', 'r')  #r for read, r is the mode
content = file.read()   #read is the method
print(content)'''
#Why absolute path didn't work - \U was interpreted as unicode escape by Python
#file = open(r"C:\Users\ASUS\PycharmProjects\Coding with Sagar\File.txt", "r")
'''content = file.read()
print(content)
file.close()'''

#Types of Modes

'''
| Mode   | Description                                                                                                   | Creates File (if not exists)? | Overwrites Existing Data? |
| ------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------- |
| `'r'`  | Read mode – Opens a file for reading only.                                                                    | No                            | No                        |
| `'w'`  | Write mode – Opens a file for writing. If the file exists, it is overwritten.                                 | Yes                           | Yes                       |
| `'a'`  | Append mode – Opens a file for writing, but data is added at the end.                                         | Yes                           | No                        |
| `'x'`  | Exclusive creation mode – Creates a file but fails if it already exists.                                      | Yes                           | No                        |
| `'r+'` | Read & Write mode – Opens a file for both reading and writing.                                                | No                            | Yes                       |
| `'w+'` | Write & Read mode – Opens a file for both reading and writing, but overwrites if the file exists.             | Yes                           | Yes                       |
| `'a+'` | Append & Read mode – Opens a file for reading and appending, preserving existing data.                        | Yes                           | No                        |
| `'x+'` | Exclusive creation with read & write – Creates a file for reading and writing but fails if it already exists. | Yes                           | No                        |
'''
#w
'''file = open("File.txt","w")
content=input("Write something for the file: ")
file.write(content)
print("Go and check updated file")
file.close()'''
#yeah, it works

#But we can't write file.close() again and again, so we have with statement

#with statement
'''with open("File.txt","r") as File:
    print(File.read())'''
#file.close() ki zarurat hi nhi padi

'''with open("Bantu.txt","w") as Bantu:
    content = input("Do shabd kahiye: ")
    Bantu.write(content)'''
#Aa gai Bantu.txt

'''with open("Bantu.txt","a") as Bantu:
    content = input("Add extra: ")
    Bantu.write(content)'''
#Appended, mode mein "a" denge, lekin method write hi rhega

#How to check if a file exists or not in your folder?

#import os
#if os.path.exists(r"C:\Users\ASUS\PycharmProjects\Coding with Sagar\Bantu.txt"):
    #print("exists")
#else:
    #print("doesn't exist")

##Lecture completed successfully :)##
















