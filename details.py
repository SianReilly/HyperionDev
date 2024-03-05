# ========= Practical Task 2 =========
# Pseudo code: 
# input users_name - string
# input users_age - string
# input users_house_number - string
# input users_street_name - string
# print out users_name + users_age + users_house_number + users_street_name
# Use f string to format it appropriately and add sentence strucutre.

# 2nd program:
# These input commands get the user's details.
# The variables are stored as strings and printed out together via an f string on a separate line.

users_name = input("Enter your name: ")
users_age = input("Enter your age: ")
users_house_number = input("Enter your house number: ")
users_street_name = input("Enter your street name: ")

print(f"This is {users_name}. They are {users_age} years old and live at house number {users_house_number} on {users_street_name}.")