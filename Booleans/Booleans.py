# when you compare two values, python gives you boolean result: True, False.

print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False


# when you run a if condition, python returns bool value: [condition]

a = 200
b = 100

if a > b:
  print("a is greater than b")
else:
  print("b is not greater than a")

# Almost every string, number, list[], tuple(), set{}, and dictionary{key:value} are True except 0, empty string, empty [], {}, (), {key:value}

# 0, empty string, empty [], {}, (), {key:value} --> these value returns False.

# the bool() function returns True, False.

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#false value
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
