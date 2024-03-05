# ========= Task 1 ===========
# Pseudocode:
# Use the if-elif-else statement structure to create the program
# Create a user input to store users age as an integer (cast)
# Else the user is under 13 print "You qualify for the kiddie discount."
# Elif the user is equal to 21 print "Congrats on your 21st!"
# Elif user enters a higher number than 100 print "Sorry, you're dead."
# Elif the user is equal to or over 65 print "Enjoy your retirement!"
# Elif the user is over 40 print "You're over the hill."
# Else if the age is anything else print out the message "Age is but a number"


# Practical Task 1:

# Requesting user input for age.
# Assigning value to variable users_age and casting it as an integer.
users_age = int(input("Please enter your age (integers only accepted).")) 

if users_age < 13:
    print("You qualify for the kiddie discount.")
elif users_age == 21:
    print("Congrats on your 21st!")
elif users_age > 100:
    print("Sorry, you're dead.")
elif users_age >= 65:
    print("Enjoy your retirement!")
elif users_age > 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")
