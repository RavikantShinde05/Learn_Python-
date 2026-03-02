# whereas "for loop" is to do iteration on iterable objects.
# While Loop: It's use to do a task the until the condition is true.

# EXAMPLE: 1

age = 100

while age > 0:
    print(age)
    age //= 2  # simple way age // 2 = age


# This a simple Example of command shell Where terminal will ask for user input
# continously untill "quit" as input.

comm = ""
while comm != "quit":
    comm = input('>')
    print("ECHO", comm)


# As the quit or Quit or QUIT means different this can cause error in this example to
# eliminate this error.

comm = ""
# this will convert all type of "quit" as valid lower case input.
while comm.lower() != "quit":
    comm = input(">")
    print("ECHO", comm)


# Infinite Loop: Be cautious while using these a they run forever so you always have a way to break the loop.
# these type of programms are heavy may cause memory to crash.
while True:
    comm = input(">")
    print("ECHO", comm)
    if comm.lower() == "quit":
        break
