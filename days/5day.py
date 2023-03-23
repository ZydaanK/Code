# File Created by: Chris Cozort


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

def adder(x,y):
    return x > y
# prints what 5 + 12 is in the terminal
print(adder(5,12))


def evaluate(x,y):
    return x > y

print(evaluate(24,13))


def evaluate(x,y):
    if x > y:
        return x > y
    else:
        return "NOPE"
print(evaluate(4,19))