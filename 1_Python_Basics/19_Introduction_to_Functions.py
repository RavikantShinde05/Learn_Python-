# function is created with the help of keyword usning "def":

def greet():
    print("hello")
    print("The internet World")


greet()


# use this "-> None" if your function is not returning any value or just printing the output:
def greet1() -> None:
    print("Hi")
    print("digital world")


greet1()


# here "First_name"and "Last_name" are the parameters and "Albus", "Dumbledor" is an arguments to this function:

# PARAMETERS: are the inputs defined for the funtion which require values Whereas.
# ARGUMENTS: Are the actual values for the given PARAMETERS.
def greet2(First_name, Last_name) -> None:
    print(f"Hi {First_name} {Last_name}")
    print("its nice to meet you")


greet2("Albus", "Dumbledor")  # both the parameters are mandetory.


# OPTIONAL PARAMETERS IN FUNCTIONS:
# there are 2 types of functions that are:
# 1. functions perform a task like print():
# 2. funcitons that Calculate and return values:

# Example 1 :
def greet3(name) -> None:
    print(f"the work is done by {name}")


greet3("Albert")
# don't leave the argument empty if parameters are provided in the function


# instead of do this:
# here the return keyword is used so we should not use None in the function:
def greet4(name):
    return f"this work is done by {name}"


greet4("Albert")


# Example 2 :
def greet(name) -> None:  # this none represents absence of value.
    print(f"Hi {name}")
# this function just prints the name on the terminal and can not be reuse or customize the message
# or we can not customize the message so we need to create another function means we cannot reuse


def get_greet(_name):
    return f"HI {_name}"
# this form of the function is not printing something on terminal instead
# it returns the Calculate value for futher operations.
# This is more reuseable and can be used in multiple ways


message = get_greet("Robin")
# here we can do more operation like print etc with the message or returned value.
print(message)
