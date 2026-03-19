def inc(number, by):
    return number + by


# instead of writing like this:
result = inc(5, 1)
print(result)  # output is 6

# write this:
# we can write this in otherway also as it returns value at output like below.
print(inc(5, 1))  # output is 6


# or can be written as
# Here by=1 is a "KEYWORD ARGUMENT" AND the code is more readable.
print(inc(5, by=1))
