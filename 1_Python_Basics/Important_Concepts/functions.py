from datetime import datetime

print('Here is the current Date and Time')
print(datetime.now())  # To Print the current date and time.

# to print current date and time we have to write this code repeatedly so to increase the reusablity.
# use "def" for define a function.


def current_dateTime() -> None:  # indentation is must
    print('Here is the current Date and Time')
    print(datetime.now())


current_dateTime()  # call the function now as many times as need.

# to make this functions more cutomizable or can be called anywhere for
# different variables on different files.


def monitor(name: str) -> None:  # if your function does not return anything or any Value use None
    print(f"hello, {name}")


monitor("David")

# to call it on other page:
monitor('Harry potter.')

# Another example like an mathematical equation.

# Example : 1


# float is the value in return using return keyword or else use None
def add(a: float, b: float) -> float:
    return a + b


print(add(1, 2))
# or recall the function for other file.
print(add(5, 6))


# Example : 2

def sub(a: int, b: int) -> None:  # no return keyword then use None.
    print(f'here is the sub value {a - b}')


sub(11, 6)  # output: here is the sub value 5
