x = 999999999999
print (x)

x = 1.2
y = -5.6
z = 3.2e2
print (type(x))
print (y)
print (z)

x = 3+5j
y = 5j
z = -5j
print (type(x))
print (y)
print (z)

print()
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print()

#Random Number
import random
print(random.random())

print(random.randrange(1, 10))