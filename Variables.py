print("Variables used to store value/data:")
print()
my_name = "Silky"
my_number = 5
my_height = 5.5

print(my_name)
print(my_number)
print(my_height)
print()
print("Get the Type of variable with the type() function: ")

print(type(my_name))
print(type(my_number))
print(type(my_height))

print()
#output:
# <class 'str'>
# <class 'int'>
# # <class 'float'>

print("Creating Variables casting:")
my_name = int(5)
my_number = str(5) #store 5 as a string not a integer
my_height = float(5) 

print(my_name)
print(my_number)
print(my_height) #5.0

print()

print(type(my_name))
print(type(my_number))
print(type(my_height))

print()
#output:
# <class 'int'>
# <class 'str'>
# <class 'float'>


#Naming convensions:
#1. Lower case : myfirstname
#2. Camel case: myFirstName
#3. Pascal case: MyFirstName
#4. Snake case: my_first_name

# Assigning multiple variable at once

x, y, z = "apple", "cherry", "banana"
print(x)
print(y)
print(z)

print()

x = y = z = "apple"
print(x)
print (y)
print (z)

print()

fruits = "Apple", "Cherry", "Banana"
x, y, z = fruits
print(x)
print (y)
print (z)

print ()
# use + to add variables

x = "I love"
y = " Python"
print(x+y)

print ()

print("If you try to combine a string and a number, Python will give you an error: check example")

# x = 5
# y = " Python"
# print(x+y)
print ()
print("Global variable: it is useful when we create function.")
#Global variables can be used in both inside and outside of functions.

value = 10 #global variable

def myfunc():
  value = 5 #local variable
  print(value)

print(value) #print 10
myfunc()  #print 5

#Create a variable outside of a function, and use it inside the function

message = "Interesting!"

def myfunc():
  print("Python is " + message)

myfunc()

#Create a variable inside a function, with the same name as the global variable

message = "Awesome!"

def myfunc():
  message = "fantastic!"
  print("Python is " + message)

myfunc()
print("Python is " + message)