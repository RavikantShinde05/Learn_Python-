# FORMATTED_STRINGS:

first_name = "Harry"
last_name = "Potter"

# 1. Concatenated String:
full_name1 = first_name + " " + last_name
print(full_name1)  # Harry Potter

# 2. Formated String:
full_name2 = f"{first_name} {last_name}"
print(full_name2)  # Harry Potter

# 3. To get Length of String:
full_name3 = (len(f"{first_name} {last_name}"))
print(full_name3)

# 4. To get Length of individual string variables
full_name4 = f"{len(first_name)} {len(last_name)}"
print(full_name4)

# 5. Ramdom experessions are also valid in between "{}"
full_name5 = f"{first_name} {2 + 2}"
# when using formatted strings you can put any valid expressions.
print(full_name5)
