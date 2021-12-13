

#looping through list
fruits = ["apple", "banana", "kiwi"]
for x in fruits:
  print(x[0], "==")
  print(x)  
 
  
print()
#looping through string
#print all the characters of the string

fruit = "apple"
for x in fruit:
  print(x)

print()

for x in range(1, 11):
  print(x)

for x in range(11):
  print(x)



#The break Statement
#breakout the loop 


print()

for x in "Hello":
  if x == "l":
    break     #it will break the loop when x reach == l.
  print(x)  # print He

print()

# example:
fruits = ["apple", "banana", "kiwi"]

for x in fruits:
  if x == "kiwi":
    break
  print(x) # print apple banana

#The continue Statement

#With the continue statement we can stop/skip the current iteration of the loop, and continue with the next
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # print apple cherry

print()


for x in "Hello":
  if x == "l":
    continue     #it will skip the loop when x reach == l and continue with next
  print(x)  # print heo