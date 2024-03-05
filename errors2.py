# ========= Task 1.2 ===========
# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Runtime Error= TypeError - lion needs to be in string format
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# SyntaxError - needs to be formatted into a f string
# Logical Error - number of teeth and age needs to be written clearly.
full_spec = (f"This is a {animal}. It has {number_of_teeth} teeth and it is a {animal_type}.")

# SyntaxError: Missing parentheses in call to 'print' = added ()
print (full_spec)