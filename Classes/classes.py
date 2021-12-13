#To create a class, use class keyword :

class my_class():
  #create variable
  x = 10
  #create function
  def my_func(self):
    print("I am inside my_class class")
    
  
  #to access any class, create another variable
car1 = my_class()
print(car1.x)
car1.my_func()


#init function: To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a  __init__() function, which is always executed when the class is being initiated.

print("========================")

# question: Create a class named Person, use the __init__() function to assign values for name and age:

class Person():
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city
  
  def my_func(self):
    print("The name of the person is", self.name, "who is", self.age, "years old and lives in",self.city)
person1 = Person("Silk", 38, "malmö")
#using person1 i can access the name and age of the person 
print(person1.name)
print(person1.age)
print(person1.city)
#call the function using person1
person1.my_func()
#The __init__() function is called automatically every time the class is being used to create a new object.

  
  

