# Create a function that takes a name as an argument and returns a new string that says Hello and then the name that was the argument
# Use this function and ask the user for their name and tell them Hello

print("John")

name = "John"
print (name)

print("Hello", name)
print("Hello " + name)
hello_john = "Hello" + " " + name
print(hello_john)

print("Our function is defined below")
def sayHelloPrint(the_users_name):
    print("Hello " + the_users_name)

print("Using our function with the print statement inside")
sayHelloPrint("John")
print(sayHelloPrint("John"))

def sayHelloReturn(the_users_name):
    return "Hello " + the_users_name

print("Using our function with the return statement inside and not printing")
sayHelloReturn("Steve")

print(sayHelloReturn("Steve"))

users_name = input("What is your name? ")
print(sayHelloReturn(users_name))