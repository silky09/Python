print("Data types: ")
print("1. Text: str")
print("2. Numeric: int, float, complex")
print("3. Sequence: list, tuple, range")
print("4. Mapping: dict")
print("5. Set: set, frozenset")
print("6. Boolean: bool")
#print("7. Binary: bytes, bytearray, memoryview")

print()
print("1. Text: str")
x = "Hello"
print(x)
print(type(x))

print()
print("2. Numeric: int, float, complex")
x = 5
y = 5.5
z = 5j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

print()
print("3. Sequence: list, tuple, range")
x = ["HTML", "CSS", "PYTHON"] #list
print(x)
print(type(x))
print()
x = ("HTML", "CSS", "PYTHON") #tuple
print(x)
print(type(x))

print()
x = range(6) #range
print(x)
print(type(x))

print()
print("4. Mapping: dict")
#for dict, we need to give key & value
x = {
  "Name": " Silky",
  "Age": 37,
  "Place": "Sweden"
}
print(x)
print(type(x))
print()

print("5. Set: set, frozenset")
x = {"HTML", "CSS", "PYTHON"}
print(x)
print(type(x))
x = frozenset({"HTML", "CSS", "PYTHON"})
print(x)
print(type(x))

print()
print("6. Boolean: bool")
x = 5
y= 4
print(bool(x == y))
#print(x < y)
print(type((x < y)))
