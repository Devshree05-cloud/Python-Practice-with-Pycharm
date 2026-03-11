'''a =  25
b = 7.56
c = "10"
print(type(a))
print(type(b))
print(type(c))
print(a+int(c))
print(str(a)+c)'''

'''txt = "Python Programming"
print("p".casefold() in txt.casefold())
#Case sensitive
print("P" in txt)
print("P" in txt and len(txt)>=18)'''

'''a =[1,2,3]
b =[3,4,5]
c =[1,2,3]
b=c
print(b) #It tells b to point to c, now in any case if you want original b back, you need to copy it somewhere else cause in python one variable points to only one value and you have given that value to b (pointing to c)
print(c)
print(a is c)
print(b is c)
print(a == c)
print(b == c )'''

'''result =3+2*2==7
print(result)
print(not(result))

a = not(True and False)
print(a)

print(result and a)

b = "py" in "python"
print(b)

print(result and a and b)
print(not(result and a and b))
print(result or a and b)'''

'''a = 10
b = 5
b = a
a+=5
c = b
print(a,b)
list1 = [a,b]
print(list1)
list1+=[c]
print(list1)'''

'''a = 12
b = 5.0
c = "7"
d = True         #d is equal to 1, you don't even need type conversion
result = (a + int(b) + int(c))*d
print(result)
print(a+d)'''

#PEMDAS
'''x = 4
y = 3
z = 2
result = x*y+z+z+z//z
print(result)'''

'''p = "hello"
q = 5
r = True
result = (p*2+str(r))*bool(q==5)
print(result)'''
#Output = hellohelloTrue

#Final problem
'''a = 256
b = 256
c = 257
d = 257
e = [1, 2, 3]
f = [1, 2, 3]
g = "hello"
h = "hello"
i = ""
j = False
print(a is b)    #True
print(c is d)     #True
print(e == f)     #True
print(e is f)      #False
print(g is h)      #True
print(g == h)      #True
print(i == j)      #False
print(not i == j)   #True
print(j or g)      #hello
print(i or j)      #False
print(i is j)       #False    Ek string ka matlab boolean nhi hota '''
'''a = 0
b = False
c = ""
d = "0"
e = "0"
f = "hello world"
g = "hello world"
h = [1, 2]
i = [1, 2]
j = 257
k = 257
l = []

print(expr1 := a == b)
print(expr2 := a is b)
print(expr3 := c == b)
print(expr4 := not c == b)
print(expr5 := d is e)
print(expr6 := f is g)
print(expr7 := h == i)
print(expr8 := h is i)    #Kyuki Lists are mutable and strings are immutable
print(expr9 := j == k)
print(expr10 := j is k)
print(expr11 := b or f)
print(expr12 := c or b)
print(expr13 := not c or b)
print(expr14 := (not c) == b)
print(expr15 := d == e)
print(c is b)
print(c is e)
print(c == l)
print(c is l)
print(a == l)
print(a is l)
print(b == l)
print(b is l)'''
#== hone ke liye pehle dono ka datatype same hona chahiye, o aur 1 to false aur true ki values hi hain isliye wo case normal hai


'''a = 0
b = False
c = ""
d = []
e = []
f = d
g = [0]
h = [0]
i = "py"
j = "py"
k = "p" + "y"
l = "".join(["p", "y"])
m = 256
n = 256
o = 257
p = 257'''
'''print(a == b)  #True    numerically same hote hain
print(a is b)  #False  ek int hai ek bool hai'''
'''print(m == n) #True
print(m is n)  #True
print(o == p)  #True
print(o is p)  #True'''
'''print(d == e)  #True     same datatype aur abhi same dikhte hain
print(d is e) '''  #False   lists mutable hoti hain, memory mein alag alg jagah create hongi
'''print(a == c)   #False   datatype hi alag hai bhai
print(a is c)   #False'''
#Same goes for
'''print(a == d)   #False
print(a is d)    #False
print(c == d)    #False
print(c is d)     #False'''
#datatypes alag ho jate hain, falsy ho jane ka matlab false hi nhi ho jata
'''print(b == d)     #False
print(b is d)     #False
print(b == c)     #False
print(b is c)     #False'''

'''print(d == g)   #False
print(d is g)   #False'''
#Since f = d
'''print(f == d)    #True
print(f is d)     #True'''

'''print(i == k)      #True
print(i is k)      #True   same datatype aur equal objects hain
print(i == l)     #True
print(i is l)'''     #False  kyuki naya hi memory space dynamically allocate hota hai function se  ---> alag hi function hai
'''print(a or b)  #False
print(b or a)  #0
print(a and b)  #0
print(b and a)   #False
print(c or d)    #[]
print(d or c)     #Space
print(c and d)     #Space
print(d and c)     #[]'''

'''print(a or c)  #empty space
print(g and h) #[0]     --->[0] was not a falsy value so it moved to next value which was also [0]
print(a and g)  #0'''
#And - x and y returns the first falsy value, if first is not falsy, it returns the second value
#Or - x or y returns the first truthy value, if first value is not truthy, it returns the second value
#And has higher precedence than Or
#Not has the highest precedence over And and Or
#[0] is not a falsy value - Ek list ke andar object hai bhai
'''print(a or b or c or d)  #[]
print(d or c or a)   #0
print(a and b and c and d) #0
print(g and a or d)    #[]
print(a or g and d)    #[]'''
'''print(i or j or k or l) #py
print(c or i and a)   #0
print(c and i or a)   #0
print(i and j and k)  #py
print(i and c or g)   #[0]'''
'''print(d or e)   #[]
print(d and e)   #[]
print(f or e)    #[]
print(f and e)   #[]
print(g or h)    #[0]'''
'''print(m or n)   #256
print(o or p)   #257
print(m and n)   #256
print(o and p)   #257
print(a or m and o)   #257'''
'''print(a or b and c or d and e)  #[]
print((i and c) or (a and g) or h)  #[0]
print((a or g) and (c or i))  #py
print(d and g or c and i or a)  #0
print(a or b or c or d or g or i)  #[0]'''

#Assigment operators again
'''print(d == e, d is e)   #True False
print(f == d, f is d)   #True True
print(g ==h, g is h)    #True False
print(i == j, i is j)   #True True
print(i == k, i is k)    #True True
print(i == l, i is l)    #True False
print(m == n, m is n)    #True True
print(o == p, o is p)   #True True'''

'''print((d == []) and (d is []))   #False
print(d is [])   #False - Same concept - Lists are mutable, d points to [] list but [] in itself will create a new object in memory space cause it is not statis
print((g == [0]) and (g is [0]))   #False
print(g is [0])       #False
print(i is "py")    #True - Because strings are immutable'''


'''x = [1, 2]
y = [1, 2]
z = x
t = (1, 2)
u = (1, 2)
s1 = "hello_world"
s2 = "hello" + "_" + "world"
s3 = "".join(["hello", "_", "world"])
n1 = 1000
n2 = 1000

print(x==y, x is y)   #True False
print(z==x, z is x)    #True True   Kitna hi dynamic ho, z to hmesha usi pr point krega na 
print(t==u, t is u)   #True True
print(s1==s2, s1 is s2)   #True True
print(s1==s3, s1 is s3)   #True False
print(n1==n2, n1 is n2)   #True True'''

'''a = [10, 20]
b = [10, 20]
c = a
d = ()
e = ()
f = (1, 2)
g = (1, 2)
s1 = "python"
s2 = "py" + "thon"
s3 = "".join(["py","thon"])
n1 = 256
n2 = 256
n3 = 257
n4 = 257

print(a==b, a is b)    #True False
print(c ==a, c is a)    #True True
print(d == e, d is e)   #True True
print(f == g, f is g)    #True True
print(s1 == s2, s1 is s2)   #True True
print(s1 == s3, s1 is s3)    #True False
print(n1 == n2, n1 is n2)    #True True
print(n3 == n4, n3 is n4)   #True True
print(a == c, a is c)    #True True
print(f == g, f is g)     #True True'''

#Loops
'''a = int(input("Enter the age:"))
if a<13:
    print("Child")

elif 13<=a<=19:    #If else hai bhai, range nhi hai... dhyan se dekh
    print("Teen")

else:
    print("Adult")'''

#Wrong Codes:

'''a = input("Enter Username:")
b = input("Enter the password:")
if a == "" or b == "":
    print("Missing Credentials")
elif len(b)<4:
    print("Weak Password")
elif b is not int:
    print("Password must be integer")
else:
    print("Login Successful!")'''


'''a = input("Enter Username:")
b = input("Enter the password:")
if a == "" or b == "":
    print("Missing Credentials")
elif b is not int:
    print("Password must be integer")
elif len(b)<4:
    print("Weak Password")
else:
    print("Login Successful!")'''

#b is always not an int (kyuki tumne hi starting se string mein convert kiya hai), so the condition is always true.

#How if works?  Checks for if-elif-else:
'''It checks for the first true statement among if and elif, if none was 
true then move to else, if anyone was true then leave all the next conditions
'''

'''x = int(input("Enter an integer:"))
if x == "":
    print("Kuchh enter kar bhai")
else:
    print(x)'''
'''You imposed integer input in the beginning, anything wrong and the code
does not ask other cases, it just crashes. So first it will take the input
as empty when you will press enter, so it took int("") first. This is 
 just wrong and the code crashes immediately.'''

#Correct code after understanding logic:

'''a = input("Enter the username:")
b = input("Enter the password:")
if a=="" or b=="":
    print("Missing Credentials")
elif not b.isdigit():
    print("Password must be integer")
elif len(b)<4:
    print("Weak password, keep at least 4 integers")
else:
    print("Login Successful!")'''

#.isdigit() is a string method in python, which checks inside the string if all the characters are integers
#Python has so many string methods (checking the string), you can google and use them
'''
I didn't get this code:
while True:
    a = input("Enter your Username:")
    b = input("Enter Password:")
    if a == "" or b == "":
        print("Enter values")
    elif len(b) < 6:
        print("Password must be at least 6 characters")
    elif not (any(ch.isalpha() for ch in b) and any(ch.isdigit() for ch in b)):
        print("At least one integer is required with alphabets")
    elif not (any(ch.isupper() for ch in b)):
        print("At least one letter should be uppercase")
    else:
        print("Valid Password entered!")
        break
    c = input("Enter your age:")
    if c == "":
        print("Enter age properly")
    elif not c.isdigit():
        print("Enter appropriate age in integer")
    elif int(c) < 13:
        print("Only above 13 candidates allowed!")
    else:
        print("Login Successful!")
'''
#Understanding if elif else:

'''maths = int(input("Enter Maths marks: "))
hindi = int(input("Enter Hindi marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))
sanskrit = int(input("Enter Sanskrit marks: "))
Percentage = (maths+hindi+english+science+sanskrit)/5
#I want the name of subject written too:
if (maths>100) or (hindi>100) or (english>100) or (science>100) or (sanskrit>100):
    print("Enter valid marks")

elif (maths<35) or (hindi<35) or (english<35) or (science<35) or (sanskrit<35):
    print("Failed!")

else:
    print("Passed!")
    print(Percentage)
    if Percentage>=90:
        print("Grade A")
    elif Percentage>=75:
        print("Grade B")
    elif Percentage >= 60:
        print("Grade C")
    elif Percentage>=40:
        print("Grade D")'''

#Slightly advanced code:
'''maths = int(input("Enter Maths marks: "))
hindi = int(input("Enter Hindi marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))
sanskrit = int(input("Enter Sanskrit marks: "))
Percentage = (maths+hindi+english+science+sanskrit)/5
failed_subjects=[]
if (maths>100) or (hindi>100) or (english>100) or (science>100) or (sanskrit>100):
    print("Enter valid marks")
if maths<35:
    failed_subjects.append("Maths")
    
#The use of elif would be wrong here cause it says that "check only if previous was false, which isn't logical cause a student could fail in multiple subjects

if hindi<35:
    failed_subjects.append("Hindi")
if english<35:
    failed_subjects.append("English")
if science<35:
    failed_subjects.append("Science")
if sanskrit<35:
    failed_subjects.append("Sanskrit")
if failed_subjects:
    print("Failed in","".join(failed_subjects))
else:
    print("Passed!")
    print(Percentage)
    if Percentage >= 90:
        print("Grade A")
    elif Percentage >= 75:
        print("Grade B")
    elif Percentage >= 60:
        print("Grade C")
    elif Percentage >= 40:
        print("Grade D")
'''
#Next Problem:
'''age = int(input("Enter your age:"))
has_id = input("Do you have ID[True/False]:").casefold()
#.casefold() converts the input to lower case, so no matter what the user types, it would be "false"
hour = int(input("What is this hour in the range of 0 - 23:"))
if (age<18) or (has_id=="false") or (hour<9 or hour>18):
    print("Access Denied!")
else:
    print("Access Granted!")'''

#Next Problem - Smart Eligibility and Scholarship Assessment System
'''attendance = float(input("Enter attendance percentage:"))
meds = input("Do you have medical certificate?[True/False]").casefold()
disc = input("Any disciplinary action against you?[True/False]").casefold()
if attendance<0 or attendance>100:
    print("Enter valid attendance!")
    exit()
elif disc=="true":
    print("Disqualified due to misconduct")
    exit()
elif attendance<75 and meds=="false":
    print("Not eligible for exam")
    exit()
else:
    print("Eligible for the exam")

avg = float(input("Enter average marks"))
if avg < 0 or avg > 100:
    print("Enter valid average marks!")
elif avg < 40:
    print("Failed!")
elif avg >= 85 and attendance >= 90:
    print("Merit Scholarship")
elif avg >= 60 and attendance >= 95:
    print("Attendance Scholarship")
else:
    print("Passed!")
    print("No Scholarship")'''
#Learnt the use of exit() function

#Next Problem - Smart Loan Approval and Risk Assessment System
#Wohoo!! Correct Handwritten code below

'''age = int(input("Enter your age:"))
income = float(input("Enter your monthly income:"))
credit = int(input("Enter credit score:"))
loans = input("Existing loans?[True/False]").casefold()
crime = input("Any Criminal Record?[True/False]").casefold()

if age<18:
    print("Invalid Application!")
    exit()
elif income<=0:
    print("Invalid Application!")
    exit()
elif credit<300 or credit>850:
    print("Invalid Application!")
    exit()
elif crime == "true":
    print("Loan rejected!")
    exit()
elif credit<450:
    print("Loan rejected")
    exit()
elif (credit>=450) and (credit<=599) and income<50000:
    print("Loan Under Review")
    exit()
else:
    print("Loan Approved!")
    if credit >= 750 and loans == "false":
        print("Interest Rate:6%")
        if credit>=750 and income>=100000:
            print("Risk: Low Risk")
            exit()
        elif credit>=650 and income>=60000:
            print("Risk: Medium Risk")
            exit()
        else:
            print("Risk: High Risk")
            exit()
    elif credit>=700:
        print("Interest Rate:8%")
        if credit >= 750 and income >= 100000:
            print("Risk: Low Risk")
            exit()
        elif credit >= 650 and income >= 60000:
            print("Risk: Medium Risk")
            exit()
        else:
            print("Risk: High Risk")
            exit()
    else:
        print("Interest Rate:10%")
        if credit >= 750 and income >= 100000:
            print("Risk: Low Risk")
            exit()
        elif credit >= 650 and income >= 60000:
            print("Risk: Medium Risk")
            exit()
        else:
            print("Risk: High Risk")
            exit()'''

#Improved code by Chatgpt:
'''age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit = int(input("Enter credit score: "))

loans = input("Existing loans? [True/False]: ").casefold() == "true"
crime = input("Any Criminal Record? [True/False]: ").casefold() == "true"

# ---- Validation ----
if age < 18:
    print("Invalid Application!")
    exit()

elif income <= 0:
    print("Invalid Application!")
    exit()

elif credit < 300 or credit > 850:
    print("Invalid Application!")
    exit()

# ---- Rejection ----
elif crime:
    print("Loan rejected!")
    exit()

elif credit < 450:
    print("Loan rejected!")
    exit()

# ---- Under Review ----
elif 450 <= credit <= 599 and income < 50000:
    print("Loan Under Review")
    exit()

# ---- Approved ----
else:
    print("Loan Approved!")

    if credit >= 750 and not loans:
        print("Interest Rate: 6%")

    elif credit >= 700:
        print("Interest Rate: 8%")

    else:
        print("Interest Rate: 10%")
    #Antar itna hai ki exit nhi liya hai yahan se!
    # ---- Risk ----
    if credit >= 750 and income >= 100000:
        print("Risk: Low Risk")

    elif credit >= 650 and income >= 60000:
        print("Risk: Medium Risk")

    else:
        print("Risk: High Risk")'''

#Beginning For Loop
'''for i in range(1,5):
    for j in range(1,3):
        print(i,j)
        print(j,i)'''
'''for i in range(1,5):
    for j in range(1,3):
        print(i,j)
    print(j,i)'''
'''for i in range(1,5):
    for j in range(1,3):
        print(i,j)
    print(j,i)
print(i,j) '''
'''for i in range (1,8):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
for i in range (1,8):
    if i == 2:
        continue
    if i == 5:
        break
print(i)'''
#Security Scan System
'''for i in range (1,4):
    for j in range (1,6):
        if i == 2 and j == 3:
            continue
#print(i,j) to code ka pura execution krta hai, continue uske pehle aana chahiye
        print(i,j)
        if (i, j) == (3, 4):
            print("Scanning Stopped!")
            break
    if i==3:
        break'''
        #Nearest yani starting wala for loop todna hai kyuki usi ke if mein break hai
#exit() is a program killer - it stops the entire program immediately
#Meanwhile break exits the nearest loop only - There are two different types of breaks depending upon use cases - inner break and outer break

#Exam Evaluation System
'''for x in range (1,4):   #x represents centers
    for y in range (1,7):  #y represents students
        if x==1 and y==2:
            continue
        if x==2 and y==5:
            break
        if x==3 and y==4:
            break
        print("Checking center",x,"student",y)'''

#For changed ranges of x and y and then putting limitation to a for under another for, we will need outer loop break function
'''for x in range (1,7):   #x represents student
    for y in range (1,4):   #y represents centers
        if x==2 and y==1:
            continueh
        if x==5 and y==2:   #confusion
            break
        print("Checking student",x,"at Center",y)
#Condition - Stop everything when student 4 reaches center 3 
    if x == 4:
        break'''

#if else elif again
'''a = input("Enter your role [intern, employee, manager, admin]").casefold()
b = int(input("Years of experience in the company?"))
c = input("Are you on probation [True/False]").casefold()
d = int(input("What is your security clearance in the range of 1 to 5?"))
e = int(input("What is the login time from 0 - 23?"))

if a == "admin":
    if c=="true" or d<4:
        print("Limited access")
    else:
        print("Full access")

elif a == "manager":
    if (b>=5) and d>=3:
        print("Full access")
    else:
        print("Limited access")

elif a == "employee":
    if 9<=e<=18:
        print("Limited access")
    else:
        print("Temporary access")

elif a == "intern":
    if d>=3:
        print("Temporary access")
    else:
        print("No access")'''

#Read that gr8 if elif else problem again (revision)

#For loop:
#The Grid Problem
'''i = 0
for day in range(1,11):
    for time in range(1,11):
        if (day+time)%3==0 and (day*time)%4 != 0:
            print("Valid Cell")
            print("Activity Score: ", day*time)
            i=i+1
        else:
            print("-----")
print(i)'''

#The above code was slightly wrong
#Correct code and understanding:
'''for day in range(1, 11):
    i = 0        #inside the day loop, i.e., will reset of each day

    for time in range(1, 11):
        if (day + time) % 3 == 0 and (day * time) % 4 != 0:
            print(day * time, end=" ")
            i += 1
        else:
            print("--", end=" ")

    print()                # moves to next row in output
    print("Valid cells in this day:", i)'''

#How print and end work?
#print() - It tells to start the next command from new line in the output
#end = " " - It tells that after printing, don't go to a new line, just add a space

#Multi-Layer Evaluation Grid
#row*col is the activity value
'''largest=0
Act_val=0
for row in range(1,10):
    i=0
    row_sum=0
    for col in range(1,10):
        #cell level logic
        if (row+col)%4==0 and (row*col)%3==0 and (row*col)%6!=0 and (row-col)!=0:
            Act_val=row*col
            print(Act_val,end = " ")
            i=i+1
            row_sum=row_sum+(row*col)
            if Act_val > largest:
                largest = Act_val
        else:
            print("XX",end = " ")
    print(i)   #row level logic
    print()
    print(row_sum)
print(largest)'''

'''Where a variable is UPDATED

Cell-level values → updated inside the inner loop
Row-level summaries → updated after the inner loop
Grid-level summaries → updated when the relevant data becomes available

✅ Where a variable is PRINTED / FINALIZED

Cell-level output → inside inner loop
Row-level output → after inner loop
Grid-level output → after outer loop'''

#Let's try pattern formation   (Wrong - Since you tried to control this)
'''for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print((4-i)*" ",i*"*")'''

#Pattern problems using gpt:

'''for i in range(1,6):
    print("*",end=" ")
print()
#Or
for i in range(5):
    print("*",end=" ")
print()
#Printing stars in a column:
for i in range(5):
    print("*")'''


'''for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()'''
'''for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
#Or (cause j has not importance while printing, just while looping
for i in range(1,5):
    for j in range(4):
        print(i,end=" ")
    print()'''

#Triangles

#This is not the real pattern work (just control logic which somehow creates that pattern)
'''for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print(i * "*")

print()

#This is the correct approach
for i in range(1,5):
    for j in range (i):
        print("*",end=" ")
    print()'''

'''for i in range(1,5):   
    for j in range(i):
        print("*",end=" ")
    print()'''

#Number Triangle:
'''for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

#Notice the output of this code:
1 
2 2 
3 3 3 
4 4 4 4 '''

#If you are giving conditions then you are somehow adjusting pattern which won't work longer, you need to just define such loops
'''for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''

#Understanding the meaning of j's range:
'''for i in range(1,5):
    for j in range(1,i):
        print("*",end=" ")
    print()
    
#Output

* 
* * 
* * * '''

'''for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()

#Output
* 
* * 
* * * 
* * * * '''

#Reverse and inverted patterns:

#My logic:
'''for i in range(1,5):
    for j in range(5-i):
        print("*",end=" ")
    print()
'''
#GPT
'''for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''

#Inverted Number Triangle:
#My code
'''for i in range(4,0,-1):
    for j in range(i):
        print(j+1,end=" ")   Ek ek j element pr condition lag rhi hai
    print()

#GPT
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

#Right-aligned triangle
'''for i in range(1,5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''

#The two inner loops run one after the other

#Pyramid
#My code
'''for i in range(1,5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for l in range(i-1):
        print("*",end=" ")
    print()'''
#GPT - Simpler code using formula
'''for i in range(1,5):
    for s in range(4-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()'''

#Printing diagonal
#My code
'''for i in range(1,5):
    for s in range(i-1):
        print(" ",end=" ")
    for j in range(1):
        print("*",end=" ")
    print()'''

#GPT - using conditional statement
'''for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#The X pattern (Pattern 12 on gpt) - Use conditional statements
#My code
'''for i in range(1,5):
    for j in range(1,5):
        if i==j or j==5-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
#And, Or ka dhyan rkhein (Revise)
#And false condition dhundhne ke pichhe - kaam hi nhi krna
#Or ko true condition chahiye, ek aur zyada bhi chalengi(Inclusive Or)

#Beginning While Loop

'''First of all the difference between for and while loops
Programmers think:
FOR = “I know how many times”  (itni hi baar)
WHILE = “I don’t know when it will stop” (utni baar jab tak condition true hai)'''

'''i=1
while i<=10:
    print(i)
    i=i+1'''

'''i=10
while i>=1:
    print(i)
    i-=1'''
#Infinite loop
'''i=0
while i<1:
    print(i)
'''
#Controlled Infinite Loop
#A loop that prints "Running" exactly 5 times, using while True

#Normal Code

'''i=0
while i<5:
    print("Running")
    i+=1'''

#Using break
'''i=0
while True:   #Just keep running this condition
    print("Running")
    i+=1
    if i==5:
        break'''

#Sum until user enters zero - Here, we don't know how many times just know until which condition is true, so we will use while loop
#My code
'''sum=0
while True:
    a = int(input("Enter an integer:"))
    if a == 0:
        break
    else:
        sum = sum + a
        print(sum)'''
#The else condition is not needed here, break does the work
#And print the result at the end after the procedure is over
'''sum = 0
while True:
    a=int(input("Enter an integer:"))
    if a == 0:
        break
    sum=sum+a
print("Total: ",sum)'''

#Age validation system

#Wrong code
'''while True:
    a = input("Enter your age: ")   #Here user input is a string
    if a!="" and a.isdigit() and a>=0:   #Now you are treating string like an integer while giving conditions
        break'''
#Fix it
#Minimum change (still the code has minute bugs)
'''while True:
    a = input("Enter your age: ")
    if a!="" and a.isdigit() and int(a)>=0:
        break'''

#Better code by chatgpt (I learnt about while more)
'''while True:
    a = input("Enter your age: ")
    if a == "":
        print("Enter a value")
        continue
    elif int(a)<0:
        print("Invalid age")
    elif not a.isdigit():
        print("Age must be an integer")
    else:
        print("Valid age")
        break'''
#Even the above code is problematic

'''Problem
input() always gives string
If I check int(a) before → program crashes
"-4".isdigit() is False, -4 is not even considered as an integer in this function use, so it just prints the statement below isdigit condition meanwhile the print statement below <0 condition should have been printed 
Any order of the last two conditions cause problem'''

#So back to try and exception handling
'''if else prevents errors by checking conditions in advance 
try except handles errors after they occur'''

'''Three conditions
Value blank na ho
Value integer hi ho
Value 0 se chhoti na ho (matlab integer to hai ye maan liya hai yahan)'''

'''while True:
    a = input("Enter your age: ")
    if a == "":
        print("Enter a value")
        continue
    try:
        age = int(a)   #Ek naya age variable hai jo ye maan rha hai ki a integer mein convert hoga, try except se program crash nhi hoga yahan
    except ValueError:
        print("Age must be an integer")
        continue
    if age<0:
        print("Invalid age")
    else:
        print("Valid age")
    break'''

#Some break and continue problems
'''Problem 1
Write a program that prints numbers from 1 to 20, but does not
print numbers divisible by 3.'''

'''for i in range(1,21):
    if i%3==0:
        continue
    print(i)'''

#While loop (confused about the placement of i+=1)

'''Rule no.1 - condition satisfy hone pr continue ke niche wala loop ka pura
code ignore hoga, condition satisfy nhi hone pr sidhe poora if ignore hoga'''

'''i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i)'''

'''i = 1
while i < 21:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1'''

'''Problem 2

Print numbers starting from 1.
Stop printing when the number reaches 10.'''

#break will be used
#Stupid approach
'''for i in range(1,11):
    print(i)'''
'''i=1
while True:
    if i==11:
        break
    print(i)
    i+=1'''

'''Problem 3

Print numbers from 1 to 15.
Skip printing even numbers.'''

'''for i in range(1,16):
    if i%2==0:
        continue
    print(i)'''

'''i=1
while i<16:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1'''

'''i=0
while i<15:
    i+=1
    if i%2==0:
        continue
    print(i)'''

'''Problem 4

Print numbers starting from 1.
Stop the loop when a number divisible by 7 is encountered.'''
'''i=1
while True:
    if i%7==0:
        break
    print(i)
    i+=1'''
'''Problem 5

Print numbers from 1 to 30 such that:
From 1 to 30:
Before 23
→ do not print numbers divisible by 5
From 23 onward (including 23)
→ print everything normally
→ no skipping rule anymore'''

#Simpler problem

'''i=1
while i<31:
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1
    if i==24:
        break'''

#Actual problem 5:
'''i=1
while i<31:
    if i<23:
        if i%5==0:
            i+=1
            continue
        print(i)
        i+=1
    else:
        print(i)
        i+=1'''
#Better code:
'''i=1
while i<31:
    if i<23 and i%5==0:
        i+=1
        continue
    print(i)
    i+=1'''

'''Problem 6

Using a while loop, print numbers from 1 upward.
Stop the loop when the number exceeds 12.'''
'''i=1
while True:
    print(i)
    i+=1
    if i==12:
        break'''

'''Problem 7

Using a loop, print numbers from 1 to 20.
Skip numbers divisible by both 2 and 3.'''
'''i=1
while i<21:
    if i%2==0 and i%3==0:
        i+=1
        continue
    print(i)
    i+=1'''

'''Predict the output:
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end=" ")
'''
#Functions
'''def book_ticket(name,city,price=500):
    print(f'Ticket booked for {name} to {city} at Rs.{price}')
book_ticket("Rahul",city="Delhi")'''
#Using return statement
'''def book_ticket(name,city,price=500):
    stat = f'Ticket booked for {name} to {city} at Rs.{price}'
    return stat
print(book_ticket("Rahul", city="Delhi"))'''

#Difference between print and return
'''def add (a,b):
    return a+b
print(add(2,3)) '''  #add likhne pr code us function se jakr output laa rha hai, mtlb function kuchh return kr rha hai
#Also note - return immediately exits the function (function mein iske niche dhyan hi nhi diya jata)

'''def add(a,b):
    print(a+b)
add(2,3) '''  #Function call ho rha hai do arguments ke liye aur unka output print ho rha hai

#Smart Order System
#Wrong code
'''total_orders = 0
def track_orders(place_orders):
    def orders():
        print("Processing order....")
        place_orders()
        print("Order Processed!")
        return orders
@track_orders
def place_orders(name,item,price=100):
    print(f'Order placed: {name} ordered {item} for Rs.{price}')
place_orders("Devshree","Pizza")
'''
'''def say_hello():
    print("Hello, Python!")
say_hello()'''

'''def greet(name):
    print(f'Hello {name}, welcome!')
greet("Devshree")
greet("Kapil")
greet()   #This will show error'''

'''Return statement does two things immediately:
Sends a value back to the caller
Stops the function right there (function exits)
Nothing after return runs.'''

'''def add(a,b):
    print(a+b)
add(5,3)
result = add(4,2)   #6 printed as it was function's work, and function is called here
print(result)    #none printed as function never returned the value, therefore nothing stored in result'''

#None - No value at this place

'''def welcome(name):
    return f'Welcome, {name}'
hey = welcome("Devshree")
print(hey)'''

'''def multiply(a,b):
    return a*b
result = multiply(4,5)  #Output top wale function ke naam se hi jana jayega
print(result)
print(int(result)+10)'''

'''def check_temperature(temp):
    if temp>30:
        print("Hot")
    elif temp<15:
        print("Cold")
    else:
        print("Normal")
check_temperature(10)
check_temperature(20)
check_temperature(35)'''

#Local Variable Isolation
'''def loc():
    message = "Hello"
    print(message)
loc()    #prints Hello as here the function is called
print(message)  #error - message is not defined, as it was a local varialbe'''

#Accessing global variable
'''city = "Mumbai"
def bhai():
    print(city)
bhai()
print(city)  #Program ran properly'''

#Shadowing a global
'''x = 100
def bro():
    x = 50
    print(x)
bro()   #50
print(x)  #100'''

#Modifying global variables - for modification, we need to call the variable using the word "global"
'''count = 0
def modi():
    global count      #For modification, this step needs to be done
    count=count+1
    print(count)
modi()   #prints 1 
print(count)     #value modified to 1 as change was made in global'''

#Read but don't modify
'''score = 10
def read():
    print(score)
read()
print(score)'''

#Multiple functions using same global
'''balance = 1000
def deposit(amount):
    global balance
    print(f'Total balance: {balance}')
    balance=balance+amount
    return balance
print("So after deposit:",deposit(4000))
def withdraw(amount):
    global balance
    print(f'Total balance: {balance}')
    balance=balance-amount
    return balance
print("So after withdrawal:",withdraw(3000))'''
#Now I understood the difference between print and return more

#Nested scope - outer and inner function
'''a = 500
def outer():
    a = 300
    def inner():
        print(a)
    inner()    #inner function needs to be called first
outer()    #then only outer will print something
print(a)   #No change as no modification'''

#Three levels
'''value = 100
def outer():
    value = 50
    print(value)
    def inner():
        value = 10
        print(value)
    inner()
outer()
print(value)'''

'''Output - 50
            10
            100'''

#Final scope mastery - Incorrect code (doesn't loop while password is incorrect)
#Hmein aisa code chahiye jo password galat hone pr loop chalata rhe aur shi hote hi function escape krr le, niche wala code use satisfy nhi krr pa rha
'''attempts = 0
correct = "Dev123"
def login(password):
    password = input("Enter Password:")
    if password != correct:
        global attempts
        attempts+=1
        print("Incorrect Password! Attempts made: ",attempts)
    else:
        return f'Success'
result = login(" ")
print(result)'''

#Chatgpt code
'''attempts = 0
correct = "Dev123"
def login(password):
    global attempts
    if password != correct:
        attempts+=1
        print("Incorrect Password! Attempts made: ", attempts)
        return False
    else:
        return True

while True:   #Jab function ne True return kiya hai (due to return statement)
    a = input("Enter Password: ")
    if login(a):
        print("Success")
        break'''

#Guess the outputs

#!!!My wrong thought - global count nhi likha, bahar parameter de diya.. dono mein gadbad hogi
'''count = 10
def update(count):  #keeping the parameter count creates a new local variable count inside the function
    count = count + 5
    print("Inside function:", count)

update(count)    #count to pehle se hi globally created variable tha, ye whi hai... local variable yahan tak nhi aaya 
print("Outside function:", count)'''

#Output
'''Inside function: 15
Outside function: 10'''

'''x = 5
def change(x):
    x = x + 10
    return x
change(x)
result = change(x)
print(x)  #5
print(result)  #15'''

'''x = 5
def change(x):
    x = x + 10
    return x
x = change(x)
print(x)   '''

#15

'''num = 20

def test(num):
    print("Inside:", num)

test(50)
print("Outside:", num)'''

'''Inside:50
Outside:20'''

'''count = 0

def increase(count):
    count = count + 1
    print(count)

increase(count)'''  #count is still the global variable here, the value of global variable is 0, so this value goes as argument to the parameter count, that is why you are getting the output 1 after calling function in this way

'''count = 0

def increase(count):   #new local variable count is created
    count = count + 1
    print(count)

increase(5)'''  #Then 6 will be the output, as the global and local count are not related at all

'''count = 0
def increase():
    global count
    count=count+1
    print(count)

increase()'''

'''count = 10

def show():  #Note - Global variable ko jab modify krna ho tabhi explicitly call krne ki zarurat hai function ke andar
    print(count)

def change():
    count = 50

change()
show()

#change mein kuchh nhi
#show mein 10'''

'''count = 10  
def change():
    print(count)
    count=50  #Is line pr aate hi python confuse ki matlab upar wali line mein local variable count ki baat ho rhi thi, pr phir to print statement baad mein aana chahiye tha, ye sequence galat hai, code galat hai => Error
change()'''

'''count = 10
def change():
    global count     
    print(count)
    count = 50     #yahan pr global count ka modification ho jata hai 
    print(count)
change()'''

#Output - 10 50
#Sequence of statements matter a lot
#Agr python ko kisi function ke andar global variable ke naam ka koi dusri value ke sath assigned dikha gaya to pehle to wo wahan local variable hua, usmein error aa skta hai

'''count = 10
def change():
    print(count)   #Seedhe global variable
change()'''
#Ouput - 10

'''my_list = [1, 2, 3]
def modify(lst):
    lst = [10, 20]
    print(lst)

modify(my_list)   #andar ke argument se koi mtlb hi nhi hai kyuki function ke andar rigidly assign kiya gaya hai
print(my_list)'''
'''Output - [10, 20]
            [1, 2, 3]'''

'''a = int(input("Enter your age: "))
def is_adult(age):
    if age>=18:
        print("Allowed")
    else:
        print("Not allowed")
is_adult(a)'''

'''x = 100
def outer():
    x = 50
    def inner():
        print(x)
    inner()
outer()'''
#50 would be printed

'''x = 100
def outer():
    x = 50
    def inner():
        x = 10
        print(x)   #10
    inner()
    print(x)    #50
outer()
print(x)     #100'''

#Pay attention here:

'''value = 5
def update(value):
    global value
    value = value + 10
    return value
print(update(20))
print(value)'''

#The above function gives an error, cause first you are saying value is a parameter and then you are calling the same name of global, this can't be done
#we gave the argument 20 for the placeholder value which the function had made a local variable, but python saw the same name of global variable being called, and it generated an error...
#Parameters are local variables

'''You are logically saying two opposite things:
value is a parameter → meaning:
“Create a new local variable called value.”
global value → meaning:
“Do NOT create a local variable. Use the global one.”
That is a direct contradiction.
Python refuses because allowing this would create ambiguity.'''

#Learn to solve problems using functions properly
#Simplest approach
'''n = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))
def divide(a,b):  #a aur b hi kyuki global variable ko as parameter thodi call krte hain
    if b==0:
        print("Denominator can't be zero")
    else:
        print(a/b)
divide(n,d)'''
#Using return
#Function only checks
'''n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))
def divide(a,b):
    if b==0:
        return False
    return True
if divide(n,d):
    print(n/d)'''

'''n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))
def divide(a,b):
    if b==0:
        return False
    else:
        return (n/d)
result = divide(n,d)
if result is False:
    print("Denominator can't be zero")
else:
    print(result)'''

#Making loop - User keeps entering values but we won't accept until the denominator is non zero
#Don't write parameters in the function when you are defining local variables

'''def divide(a,b):    #Function ka matlab hai sirf ek baar define krne ki zarurat hai, kisi loop mein nhi
    if b==0:
        return False
    return True
while True:   #block chalate rho, sirf break wali condition use todegi
    n = int(input("Enter Numerator: "))
    d = int(input("Enter Denominator: "))
    result = divide(n,d)
    if result is False:
        print("Denominator can't be zero")
    else:
        print(n/d)
        break'''

#Access Control Counter - I made it work (was really confused in the placement of while)
'''access_count = 0
correct = "OPEN123"
while access_count<3:
    def check_access():
        code = input("Enter password: ")
        if code==correct:
            return True
        else:
            return False
    result = check_access()
    if result is False:
        print("Failed")
        access_count+=1
    else:
        print("Success")
        break'''
#The above logic is correct but structure is immature
#Function should not be under the loop
'''access_count=0
correct="OPEN123"
def check_access():
    code = input("Enter the Password: ")
    if code==correct:
        return True
    else:
        return False
while access_count<3:
    result = check_access()  #Kyuki teen baar function ko call krna padega agar pehli condition hui to, aur us calling ke liye ye statement while loop ke andar aayega
    if result is False:
        print("Failed")
        access_count+=1
    else:
        print("Success")
        break'''

#Decorators - Add extra behavior to a function without modifying the function itself

'''x = 10
def outside():
    x = 20
    def inside():
        x=30
        return x
    inside()
    print(inside())
    return x
outside()
print(outside()) ''' #30 is printed twice because outside is executed twice
'''Output - 30 30 20'''

'''def my_dec(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper   #my_dec ki return value
@my_dec
def say_hello():
    print("Hello!")
say_hello()'''

'''def name(age):  name is a decorator func,age is a parameter !!age will receive a function
    def wrapper():  new func which has access to age
        print("Name: Devshree Sharma")
        age()  This is the original my_age func
    return wrapper  when someone calls name(something) return wrapper
@name
def my_age():
    print("Age: 21")
my_age()'''  #Python converts it to my_age = name(my_age)

#Permission system

#Function is allowed to execute on the basis of whether user enters True or False, that is where decorators are important
#You are modifying when the function is allowed to run
#Decorators are for modifying how another function executes

#I typed this code step by step - This is not mastery, but starting
'''
def ask():   #que will just exist inside the function, no need to give que as a parameter
    que=input("Do you want the profile?")
    return que
is_logged_in = ask()   #Take the function's return value and store it in is_logged_in
def permission(profile):   #A decorator doesn't take a value, it takes a function
    def wrapper():
        if is_logged_in.lower()=="yes":  #lower is a function so it must be followed by()
            print("Access granted")
            profile()
        elif is_logged_in.lower()=="no":
            print("Access denied")
            return False
    return wrapper
@permission
def dev_profile():
    print("This is Devshree Sharma's entire profile data: some link")
dev_profile()'''
#decorator is permission(something), that will work for any function inside, it does not need to be changed. Instead of profile, you can make age, password etc. Just by using @permission syntax. That's the power of decorators

#Generators - If you need something in return in a slower pace, there is no point of capturing whole memory with the stuff, that's where generators come
#A generator produces value one at a time, only when needed
#It doesn't store anything in the memory, it pauses and resumes, that pause and resume is the key

#return ki jagah yield ka use hoga
'''def gen():
    yield 1
g = gen()    
print(next(g)) '''  #Each next() resumes execution from where it stopped, this is the pause and resume

'''def count():
    yield 1
    yield 2
    yield 3
g = count()
print(next(g)) #1
print(next(g)) #2
print(next(g)) #3'''

#But the above work is manually exhausting
#So we use a for loop instead of writing print(next(g)) again and again
#Version 1
'''def count():
    yield 1   #yield doesn't stop the function below it like return
    yield 2   #Just a function object is created in memory. Such that = count => function object
    yield 3   #Python marks these yield statements as generator functions
g=count()    #generator is created. Such that = g=> generator object
print(g) - It shows => <generator object count at 0x0000010412EE8880>
for i in g:   #Replaces using print(next(g)) again and again
    print(i)'''

#Version 2, creating generator object becomes pointless here
'''def count():
    yield 1
    yield 2
    yield 3
g = count()   #No need here
for i in count():   #This version is creating two generators but using only one - this is conceptually equal to g = count() and for i in g:  
    print(i) '''

'''def count():
    yield(1,100)
g = count()
for i in count():   
    print(i)'''
#Output - (1, 100)
#Version 1 consumes the same generator object that you created... and uses it in the loop
#Version 2 creates its own generator object in the loop which has no relation with that g=count()

#Problem - Controlled Attempt System

#I wrote this whole code - slightly wrong, cause Card Blocked would be printed anyhow
'''def pro():
    i=0
    while i<3:
        a = input("Enter the pin: ")
        yield a
        i=i+1
g = pro()
for x in g:
    if x=="4321":
        print("Access granted")
        break
    else:
        print("Wrong PIN")
print("Card Blocked!")'''

#Slight improvement by gpt:
'''def pro():
    i=0
    while i<3:
        a = input("Enter the pin: ")
        yield a
        i=i+1
g = pro()
for x in g:
    if x=="4321":
        print("Access granted")
        break
    else:
        print("Wrong PIN")
else:   #The else outside for only executes if the loop finishes normally and doesn't break anywhere
    print("Card Blocked!")'''

#OOPS
'''class Car():   #Python creates a class object in memory
    def start(self):  #Python creates a function object called start
#self has no value yet. Function expects the instance (object) at its first argument
        print("Car is starting....")
    def stop(self):
        print("Car is stopping....")
car1 = Car()  #object mein class aur uski method store ki hai (memory mein ek physcial form mein aaya)
car2 = Car()
car1.start()
car1.stop()
car2.start()
car2.stop()'''

'''self represents the current instance of the class.
When you create an object from a class, self allows that object to:
access its own variables (attributes)
call its own methods'''

'''Python's internal conversion 
car1.start() => Car.start(car1)'''

#when you see x.y in python, it means - search y inside x

'''Memory Model in Python
class Car():
Python creates a class object in the memory
Inside the class, python builds the dictionary of attributes, in which it will store everything inside the class
    def start(self):
Python creates a function object in memory, with name start, parameter (place holder) self (for the current object), and you can see what it has to do below
       print("Car is starting...")
    def stop(self):
       print("Car is stopping...)
car1 = Car()
Object#1 created in memory
Python stores a reference object1.__class__=Car
car2 = Car()
Same goes, but the dictionary inside both these objects is empty
car1.start()
Python first goes for the dictionary inside car1, nothing found. So it looks for dictionary inside class
And inside class, Python finds start function
Now, Python binds start function with car1 object (because of self which told it to do so)
Python now executes it as start(car1)
car1.stop()
car2.start()
car2.stop()'''

#Very Important!! - See your 9 March Coding Notes

#Understanding the constructor - __init__

#Below code didn't work:
'''class Product:
    def properties(self, type, brand, cost):
        self.type = type  #. ka mtlb yaad hai na? - This line says to create an attribute "type" inside the current object (yaad kro dict khali hai)
        self.brand = brand
        self.cost = cost
    def tagline(self):
        print(f'This is {self.type} by {self.brand} at Rs.{self.cost}')
cloth = Product("Fashion", "Zara", 2500)
cloth.tagline()'''

#This code worked with constructor:
'''class Product:
    def __init__(self, type, brand, cost):
        self.type = type
        self.brand = brand
        self.cost = cost
    def tagline(self):
        print(f'This is {self.type} by {self.brand} at Rs.{self.cost}')
cloth = Product("Fashion", "Zara", 2500)
cloth.tagline()'''

#To make it work without constructor __init__
'''class Product:
    def properties(self, type, brand, cost):
        self.type = type
        self.brand = brand
        self.cost = cost
    def tagline(self):
        print(f'This is {self.type} by {self.brand} at Rs.{self.cost}')

cloth = Product()   #You can't directly define the attributes here, cause you didn't use the constructor __init__
cloth.properties("Fashion", "Zara", 2500)
cloth.tagline()'''

'''Without __init__, the object is created empty and a method like properties() must be called later to assign attributes to it.
With __init__, Python automatically calls the initializer during object creation, so the attributes are assigned immediately.
__init__ is simply a method that runs automatically to fill the object's data when it is created.'''

#Inheritance
'''class Student:
    def Dev(self):
        print("Dev is the class topper")
class Teacher(Student):
    def Diksha(self):
        print("Diksha is the best teacher")
yo = Teacher()
yo.Diksha()
yo.Dev()'''
#Will try with attributes - below is wrong code
'''class Product:
    def type(self, brand, cost):
        self.brand = brand
        self.cost = cost
    def tag(self):
        print(f'Le aaiye apne ghar {self.brand} sirf {self.cost} rupye mein')

class Shop(Product):
    def available(self):
        print(f'{self.brand} is available')

buy = Shop()
buy.available()
buy.type("Patanjali", 250)
buy.tag()'''
#Above code was wrong because of the execution order, available() ko call krr diya, lekin uske pehle type() ka function call krna zaruri tha kyuki usi mein "." ka use krk object ke andar attributes daale jaa rhe hain, aur wahin se self.brand aur self.cost ka sense ban rha hai

#Correct code with correct order
'''class Product:
    def type(self, brand, cost):
        self.brand = brand
        self.cost = cost
    def tag(self):
        print(f'Le aaiye apne ghar {self.brand} sirf {self.cost} rupye mein')

class Shop(Product):
    def available(self):
        print(f'{self.brand} is available')

buy = Shop()
buy.type("Patanjali", 250)
buy.available()
buy.tag()'''

'''Output 
Patanjali is available
Le aaiye apne ghar Patanjali sirf 250 rupye mein'''

#And if you didn't want to change the order, here the constructor comes in use.... now you got it

'''class Product:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost
    def tag(self):
        print(f'Le aaiye apne ghar {self.brand} sirf {self.cost} rupye mein')

class Shop(Product):
    def available(self):
        print(f'{self.brand} is available')

buy = Shop("Patanjali", 250)
buy.available()
buy.tag()'''
#Above code worked because __init__ constructor ne object creation hote hi direct attributes usmein ghused diye

#Polymorphism with classes
'''class Marks:
    def report(self):
        print("The class pass rate is 90%")
class Bantu(Marks):
    def report(self):
        print("Bantu passed")
class Vikas(Marks):
    def report(self):
        print("Vikas failed")
student1 = Bantu()
student2 = Vikas()
student1.report()
student2.report()'''
#Teeno mein function report tha, yani same naam but different print statements, inheritance bhi tha, mtlb Python ke liye full confusion ka chance. Pr object creation mein hmne class specify ki aur polymorphism ne bacha liya

#Encapsulation methods
'''class login:
    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin
user = login("Bhais", 3874)
print(user.username)
print(user.__pin)'''  #Error because of __ => Encapsulation method applied

#But you can still access, because __pin is not in user.__dict__ but in _login

'''class login:
    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin
user = login("Bhais", 3874)
print(user.username)
print(user._login__pin)'''  #shows pin

'''Explanation - Important
Because of double underscore, Python performs name mangling.
__pin  →  _login__pin
And _login__pin is in user's dict, not in login's dict... as 
Instance data → stored in object (__dict__)
Methods → stored in class (__dict__)'''
#Object is an instance of class - again

#Data Abstraction - Complex details chhupao, kaam ki baat batao

#The difference between Polymorphism and Data Abstraction is that the class marked as abstract method can never be instantiated (equated to object created)... it just forces its child classes to implement the method and only they can be used
'''from abc import ABC, abstractmethod
class Faltugyaan(ABC):
    @abstractmethod
    def suvichar(self):
        print("Kaal kre so aaj kar aaj kre so ab")
class Kaamkibaat(Faltugyaan):
    def suvichar(self):
        print("Exam hai agle mahine")
class Zaruribaat(Faltugyaan):
    def suvichar(self):
        print("Is baar ka tera CGPA 8.34 hai")
ghoshna = Kaamkibaat()
khushkhabar = Zaruribaat()
ghoshna.suvichar()
khushkhabar.suvichar()'''

'''Output
Exam hai agle mahine
Is baar ka tera CGPA 8.34 hai'''

#Wrong code below
'''from abc import ABC, abstractmethod
class Faltugyaan(ABC):
    @abstractmethod
    def suvichar(self):
        print("Kaal kre so aaj kar aaj kre so ab")
class Kaamkibaat(Faltugyaan):
    def suvichar(self):
        print("Exam hai agle mahine")
class Zaruribaat(Faltugyaan):
    def suvichar(self):
        print("Is baar ka tera CGPA 8.34 hai")
ghoshna = Faltugyaan()   #error dega yahan ki instantiate nhi krr skta
khushkhabar = Zaruribaat()
ghoshna.suvichar()
khushkhabar.suvichar()'''

#Chatgpt chat - OOPS
'''Abstract class defines a rule/interface
but leaves implementation to child classes.
So Parent Class is considered incomplete and can't be instantiated'''


















