#method:

#upper()
#lower()
#replace() replaces a string with another string
#strip() remove white space at the beginning or end
#split() turns any text into list, returns a list 

x = "hello"
print(x.upper()) #HELLO

x = "HELLO"
print(x.lower()) #hello

x = "hello"
print(x.replace("h", "J")) #hello

x = " hello world! "
print(x.strip())# returns "hello world!"

x = "Hello World!"
print(x.split()) # ['Hello', 'World!']
