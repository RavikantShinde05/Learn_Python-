# USER INPUT AND OPERATIONS BETWEEN DIFFERENT DATA TYPE:

# Use Terminal for this Script to "run":
# input is a function to get input from user.
x = input("x: ")  # here x is a string
y = int(x) + 1  # here 1 is a number only same data type can be concated.
z = 25

print(type(x))  # STRING
print(type(z))  # NUMBER

# x + 1 both have different data type and can not be concatenated or added like in JavaScript.
# So this Type of error can be solved by "type Conversion"

print(f"x: {x}, y: {y}")

# TYPE CONVERSIONS:
# int(x) converts into integer/number.
# float(x) converts into float.
# bool(x) converts into boolean.
# str(x) converts into string.


# TIPS:
# In false boolean value is:
# 0 = False
# "" - an empty string = False
# None = False

# For example:
bool(0)  # false
bool("")  # false
bool(-1)  # True
bool(1)  # True
bool("False")  # True
