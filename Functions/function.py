#1. a function is defined using the def keyword

def my_func():
  print("Hello there!")

my_func()

print()

#2. Arguments:

# You can add as many arguments as you want, just separate them with a comma.

def my_func(f_name):
  print("Hello there!", f_name)

my_func("Silky")

#working with args

def my_func(args):
  print("Hello there!", args)

my_func("Si")
my_func("Sil")
my_func("Silk")

print()

#3. Number of Arguments

def my_func(my_name, my_email, my_country):
  print("my info:", my_name,my_email,  my_country )

my_func("name: Silky"",", "gmail: s@gmail.com" ",","country: Sweden.")

#4. a function can have returns type

def my_func():
  x = 20
  y = 10
  c = x + y
  return c
print("sum is:", my_func())

def my_func(x,y):
  c = x + y
  return c
print("sum is:", my_func(20,20))

#5. input from user 

def my_func(x, y):
  c = x + y
  return c
print("sum is:", my_func(30, 30))

def my_func(x, y):
  c = x + y
  return c
x = int(input("Enter 1st_number: "))
y = int(input("Enter 2nd_number: "))
print("sum is:", my_func(x,y))


#6. reuse of function
def my_func(name):
  print("Hello", name)

my_func("silky")
my_func("son")
my_func("sonam")

#using default value 

def my_func(name ="san"):
  print("Hello", name + "!")

my_func("silky")
my_func("sona")
my_func() # print Hello san!