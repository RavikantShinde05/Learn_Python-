# SMALL QUESTIONS:
# print this output WITHOUT USING STEP IN FOR LOOP:
# 0
# 2
# 4
# 6
# 8
# we are having total 4 int in the list

# Solution:
count = 0
for number in range(10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we are having total {count} int in the list")


# WITHOUT CONSIDERING "0"
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"we are having total {count} int in the list")
