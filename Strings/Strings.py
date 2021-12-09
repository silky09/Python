print("Hello string!")
print()

#You can use three double quotes:

x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)
print()

#Or three single quotes:

x = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(x)
print()



#Looping Through a String
print("Looping Through a String:")

fruit = "Banana"
for x in fruit:
  print(x)

print()

#String Length-- use len() method/function


x = "Hello World"
print(len(x))
x = "Hello"
print(len(x))

print()

#Check String (in, not in keyword) gives boolean value
#Check if "free" is present in the following text:
x = "Hello World!"
print("Hello" in x) #True

x = "Hello World!"
print("Jello" in x) #False

x = "Hello World!"
print("Jello" not in x) # True