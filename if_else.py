
x = 40
y = 30

if x>y:
  print (x,"is greater")
elif y>x:
  print (y,"is greater")
else:
  print ("Both are equal")


  # elif == "if the previous conditions were not true, then try this condition".
   #else == else keyword catches anything which isn't caught by the preceding conditions.


x = 40
y = 100

if x > y:
  print("x is greater than y")
elif x == y:
  print("Both are equal")
else:
  print("y is grater than x")


#Short Hand If-else

x = 4
y = 10

print("x is greater") if x > y else print("y is greater")