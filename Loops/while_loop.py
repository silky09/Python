#With the while loop we can execute a set of statements as long as a condition is true.

x = 1
while x <= 10:
  print(x)
  x = x + 1 #print 1 to 10
  

print()

x = 1
while x < 10:
  print(x)
  x = x + 1 #print 1 to 9

#use of break statement

print()

x = 1
while x < 10:
  if x == 5:
    break
  print(x)
  x = x + 1 #print 1 to 4


# use continue statement

print()

x = 0
while x < 10:
  x = x + 1
  if x == 5:
    continue
  print(x)
  
   #skip 5 and continue the loop and print 1 to 10 except 5.
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10