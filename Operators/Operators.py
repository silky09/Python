# operators are use to perform operations on values and variables.

# Python divides the operators in the following groups:

# Arithmetic operators (+ - * /  %)
# Assignment operators (=  +=  -=  /=  *=)
# Comparison operators (==  !=  >  <  <=  >= )
# Logical operators (and  or  not)
# Identity Operators (is, is not)
# Membership Operators (in, not in)


# Arithmetic operators (+ - * /  %)

x = 20
y = 10

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

print()

# Assignment operators (=  +=  -=  /=  *=)

x = 10
print(x)
x = x + 5  # x = 15
print(x)
x = x - 5  # 10   15-5 = 10
print(x)
x = x * 5
print(x)
x = x / 5
print(x)
x = x % 5
print(x)

print()

# Comparison operators (==  !=  >  <  <=  >= )
#returns Bool Value

x = 10
y = 20

print (x == y)
print (x != y)
print (x > y)
print (x < y)
print (x >= y)
print (x <= y)

print()
# Logical operators (and  or  not)
  #Logical operators are used to combine conditional statements

    # and operator: 	Returns True if both statements are true	(x < 5 and  x < 10)

    #or	operator: Returns True if one of the statements is true	(x < 5 or x < 4)

    #not operator: 	Reverse the result,
    # returns False if the result is true	not (x < 5 and x < 10)

x = 10
print (x < 5 and x < 10)
print (x < 15 or x < 4)
print (not(x < 5 and x < 10))

print()

# Identity Operators (is, is not)-- returns Bool value

x = 10
y = 10
print (x is y)
print (x is not y)

print()

# Membership Operators (in, not in) -- returns bool value

x = "hello!"
print ("hell" in x)
print ("hell" not in x)