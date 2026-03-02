print(type(10))  # outpu: "int"
print(type(range(7)))  # output: "range"

# iterables: it is an object that can be looped over using a "for" loop or whose elements cna be accessed one at a time.
#  This means any object that can produce an iterator ia an iterable.

#  Many of the python Built-in "Data type" are iterables:
# "list"
# tuple
# str
# dict
# set
# range

# "Range" is an iterable:
# That why we can use it in for loop like this:-

# EXAMPLE: 1

for x in range(9):  # this means "X" have diff value on each iteration.
    print("ok")


# EXAMPLE: 2

for x in "Alice":  # "Alice" is a str.
    print(x)  # now the "Alice is iterable"


# EXAMPLE: 3

for x in [1, 2, 3, 4, 5,]:  # this list object is iterable
    print(x)

#  Creating an object "shopping_cart" and iterating the items in it.
shopping_cart = [biscuit, candy, rice, orange, oil]

for items in shopping_cart:
    print("items")
