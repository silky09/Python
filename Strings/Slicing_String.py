#Square brackets can be used to access index position of the string.
#Get the character at position 1 (remember that the first character has the position 0):

x = "Hello"
print(x[1]) #print e
print(x[0:4]) #print Hell
print(x[1:4]) #print ell
print(x[1:-2]) #print el
print(x[0:-2]) #print Hel

print(x[:5]) #print Hello
#Slice To the End
print(x[2:]) #print llo ---> it means print till the end of the text

x = "Hello World"
print(x[1:7])#print ello W   --> 7 starting from 1 (left side)

print()