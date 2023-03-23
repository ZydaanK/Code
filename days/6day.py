# File Created by: Zydaan Khan


# built in function that displays something in the terminal...
print("Hello there...")

# I am writing a great comment
# The equal sign, '=', is an operator
# we are telling the computer to assign a value to a label, x
x = 5
# Syntax error: The code cannot be read properly because of incorrect format
# example of syntax error
x != 6
# this will print True
print(x != 6)
# this will print False
print(x == 6)
# assigns a new value to 'x'
x = 6
print(x == 6)

my_name = "Zydaan"

# define a function called 'my_func' that is used to activate the pervious line of code
def my_func(name, message):
    # print("I can write functions!!!")
    # return "I can write functions!!!"
    return message + name
# calls the function a variable
print(my_func(my_name, "hello there, "))

def evaluate(x,y):
    if x > y:
        return x > y
    else:
        return "NOPE"
    
print(evaluate(6,12))

# function that gives back a message indicating a remainder when one
# number is divded into another
def find_remainder(x,y):
        return "The remainder of" + str(x) " and " + str(y) + " is " + str(x%y)

# call the function...
print(find_remainder(11,6))