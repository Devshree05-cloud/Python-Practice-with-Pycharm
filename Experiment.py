'''PEMDAS rule - Paranthesis, Exponentiation, Multiplication
division, addition, subtraction'''

#identity operator - for memory location
'''a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(b is c)
print(a is c)
print(b is not c)
print(a is not c)
print(a is not b)'''

'''#membership operator
a = {'Devshree':21,'Meena':20,'Kapil':19,'Rohit':22}
print(type(a))
print('Rohit' in a)'''

#Full explanation in notebook:

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

print(i,j)        #Loop se bahar last i (4) aur last j (2)'''

'''a = 0          #falsy in python
b = "0"        #falsy
c = []         #falsy
d = False      #ofcourse falsy
e = "hello"    #truthy
result = "0" != str and a!=1 and not c and not d   #True
result_1 = b is not str and a!=1 and not c and not d  #True
result_inv = "0" == str and a!=1 and not c and not d   #False
result_1_inv = b is str and a!=1 and not c and not d    #False
print(result)
print(result_1)
print(result_inv)
print(result_1_inv)'''

'''x = 1234
y = 1234
z = x
print(x == y)    #True
print(x is y)    #True
print(x is z)     #True
print(z == x)     #True'''

'''x = [1, 2]
y = [1, 2]
z = x
s1 = "data"
s2 = "da" + "ta"
s3 = "".join(["da","ta"])
t1 = (1000,)
t2 = (1000,)
n1 = 1000
n2 = 1000

print(x is y, x == y, x is z)    #False  True  True
print(s1 == s2, s1 is s2, s1 == s3, s1 is s3)  #True  True  True  False
print(t1 == t2, t1 is t2, n1 == n2, n1 is n2)   #True True True True
print([1,2] == [1,2], [1,2] is [1,2])  #True False
print(z.append(3), x == [1,2,3], z is x, y == [1,2])  #None True True True'''

#Concept hai pura mutable immutable ka, aur pointer ka asal matlab samajhna




