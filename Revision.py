# "" & [] are seen as falsy during logical operations
# == compares both the value and type-appropriate structure
#is compares the memory location, i.e., both the participants are pointing to the same memory location
#Comparison between "is" and "==" depends on mutable and immutable'''
#And - x and y returns the first falsy value, if first is not falsy, it returns the second value
#Or - x or y returns the first truthy value, if first value is not truthy, it returns the second value
#And has higher precedence than Or
#Not has the highest precedence over And and Or
#Not>And>Or

'''Working of if-else-elif ---> It checks for the first true statement among if and elif, if none was
true then move to else, if anyone was true then leave all the next conditions'''

'''if vs elif 
elif says:
Check this condition only if previous one is false
if says:
Check this condition anyways (used when multiple conditions can be true)'''

#Loops

#Loop variables are not equal to coordinates, they are just iteration counts
#So those were iterations of j, never positions as matrix

'''When i = 1:
That means:
The loop runs one time
During that one run:
j = 0
The loop body executes'''

'''For loop ko start, end aur iteration de do, wo iteration khud badhayega
leking while ko alag se badhane ka bolna padta hai wrna wo bas end ki
di hui condition to true rkhkr infinite loops bana dega'''

'''Difference between while and do while (while True + break)
If the condition is false, while will not let the iteration occur even once 
But do while will let the iteration occur one time even if the condition is false'''

#Coding with Sagar List and Tuple again:

#Lists and sets are mutable, tuples and strings are immutable

'''a = [1,2,3,4]   #List
b = (1,2,3,4)   #Tuple
c = {1,2,3,4}    #Set
d = frozenset([1,2,3,4])   #Frozenset
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''

#Range function:

'''a = "python"
for i in a:      #i takes each character of the string
    print(a) '''

'''print(a.find("y")) '''  #tells first occurence and case sensitive

'''a = "Python is my first language"
b = a.replace("Python", "Java")
print(a)
print(b)'''
#Strings are immutable, the replacement just creates a new string

'''str = "A-B-C"
s = str.split("-")
print(s) '''
#Split hokar ye list ke alag alag elements banenge

'''a = ["A","B","C"]
j = ("-").join(a)
print(j)
#This gave str again'''

'''a = [1,2,3]
b = [4,5,6]
print(a*2 + b*3)'''

'''a = [1,2,3,4,5,6]
b = int(input("Enter an integer: "))
if b in a:
    print("Found")
else:
    print("Noi")'''

'''a = [1,1,1,1,2,3,4,4,4,5]
for i in a:
    if a.count(i)>1:
        print(i)
print()
#To print i only once:
for i in set(a):
    if a.count(i)>1:
        print(i)'''

#As a set keeps unique values

#i is picking up each character
'''a = "python"
for i in a:
    print(i)
#Below approach gives error, it says string can't be represented as an integer
b = "java"
for j in range(b):
    print(j)'''

'''b = []
for i in range(1,11):
    a = i**2
    print(a)
    b.append(a)
print(list(b))'''

'''a = [i**2 for i in range(1,11) if i%2==0]
print(a)

b = [i for i in range(1,11) if i%2==1]
print(b)'''

'''a = "Devshree"
print("d".casefold() in a.casefold())'''   #for reliable case sensitive matching
#True

'''some commands are followed by brackets and some are not - What is the difference?
If you see ()
You are calling a function or method
You want the object to do something
If you don't see ()
You are just accessing stored data or an object reference, not executing anything'''

#Let's try
'''txt = "Hello"
print(txt.upper)
print(txt.upper())'''
'''Output 
<built-in method upper of str object at 0x0000024F91CAF150>   #accessed location info
HELLO   #executed form'''

'''txt = "hello"
a = txt.upper    #store method
print(a)        #show method
print(a())      #execute it

Output - <built-in method upper of str object at 0x000001C87235F150>  =>This is the method object
HELLO - Method executed object

print(a is "HELLO")   #a is method, "HELLO" is string => False
print(a == "HELLO")   #False'''

#String Interning in Python
'''It is an optimization and not a guarantee'''

#Case 1
'''a = "Hello"
b = "Hello"
print(a is b) #True
print(a == b)  #True'''

#Case 2 - Runtime Creation
'''a = "Hello"
b = "".join(["He","llo"])   #Runtime hai, to ek naya string object create hota hai - not same memory location
c = "".join("Hello")
print(a is b)   #False
print(a is c)   #False
print(b is c)   #False
print(b)  '''   #Returns "Hello", since b ko hm string bana chuke the so not a method

#Case 3 - Spaces Break Interning
'''a = "Hello World"
b = "Hello World"
print(a is b)   #True
print(a == b)   #True'''

'''p = "world"
a = "hello world"
c = "hello " + p
print(a is c)  #False   kyuki ye runtime mein ban rha to different string
print(a == c)  #True'''

#8th March prediction problems (is, ==, and, or, not, truthy, falsy, mutable, immutable)
#Section 1
'''a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)'''

'''a = [1,2,3]
b = a

print(a == b)
print(a is b)'''

'''a = 256
b = 256

print(a is b)'''

'''a = 257
b = 257

print(a is b)'''

'''a = "hello"
b = "hello"

print(a is b)'''

'''a = "hello world"
b = "hello world"

print(a is b)'''

'''a = "hello"
b = "".join(["he", "llo"])

print(a == b)
print(a is b)'''

##
'''a = [1,2,3]
b = a   #Ek memory space mein dono ko ek krr diya hai
b.append(4)
print(a is b)  #True
print(a)   #[1,2,3,4]
print(b)
print(a==b)  #True
#a will also get modified as b=a'''  #append() is a method that modifies

'''a = [1,2]
b = a
b = b + [4]  
print(a)   #[1,2]
print(b)   #[1,2,4]
print(a is b)  #False
print(a == b)   #False'''   #operator creates a new memory space

'''a = (1,2,3)  #Tuples are immutable
b = a
b = b + (4,)  #Modify to ho nhi skta, naya b banate hain - Le Python
print(a)
print(b)
print(a is b)  #False
print(a == b)  #False'''

'''a = (1,2,3)
b = (1,2,3)
print(a is b)  #True - cause immutable'''

'''a = [1,2,3]  #mutable
b = a.copy()  #same location pr point nhi krega, nai location
b.append(4)
print(a)
print(b)
print(a is b)  #false'''

#Section 3 - Truthy and Falsy
'''if []:   #Falsy value in Python
    print("A")
else:
    print("B")'''

'''if "":    #Falsy
    print("A")
else:
    print("B")'''

'''if "0":   #Truthy
    print("A")
else:
    print("B")'''

'''if 0:   #Falsy - Boolean ke logic mein bhi aata hai
    print("A")
else:
    print("B")'''

'''if None:   #falsy
    print("A")
else:
    print("B")'''

'''if 1:   #Truthy
    print("a")
else:
    print("b")'''

'''if [0]:   #Truthy 
    print("A")
else:
    print("B")'''

#CPython - Internal algorithm behind this (Mutable Immutable ka yahan koi connection nhi hai)

'''1. If obj has __bool__() → call it
2. Else if obj has __len__() → check len(obj) != 0
3. Else → object is True'''

'''__bool__()  → highest priority
__len__()   → fallback
default     → True'''

'''if ():  #Falsy 
    print("A")
else:
    print("B")'''

#Section 4 - And, Or, Not

'''And - x and y returns the first falsy value, if first is not falsy, it returns the second value
Or - x or y returns the first truthy value, if first value is not truthy, it returns the second value
And has higher precedence than Or
Not has the highest precedence over And and Or'''

'''print(0 or 5)
print(5 or 0)
print(0 and 5)
print(5 and 10)
print("" or "Python")
print("Python" and "")'''