# ========= Task 1.1 ===========
# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# SyntaxError: Missing parentheses in call to 'print' = added () to lines
print ("Welcome to the error program") 
print ("\n") # IndentationError: unexpected indent = indented line correctly

# Variables declaring the user's age, casting the str to an int, and printing the result
# Compilation error; incorrect space indentation
# Logical Error as variable only needs one =
# Logical Error as variable is number, so remove 'years old'
# Runtime Error= TypeError: can only concatenate str (not "int") to str, so removed int transformation
# Logical Error - sentence has no spaces, reformat as an f string
age_Str = 24
print(f"I'm {age_Str} years old.")

# Variables declaring additional years and printing the total years of age
# Compilation error; incorrect space indentation
# NameError: name 'age' is not defined = redefine age to age_Str via ctrl + f
# Runtime Errors = Type & Logical Errors - reformat as integers and () calculation for total_year calc to function.
# Logical Error = needs to be 3.5 years from now not 3 years from now. 
years_from_now = 3.5
total_years = (age_Str + years_from_now)

# SyntaxError: Missing parentheses in call to 'print' = added () to lines
# Logical Error: answer_years should be total_years, reformatted as an f string
print (f"The total number of years: {total_years}.")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# NameError: name 'total' is not defined = define as total_years
# Runtime Error = TypeError: can only concatenate str (not "int") to str = need to reformat as an f string
total_months = (total_years * 12)
print (f"In 3 years and 6 months, I'll be {total_months} months old.")

#HINT, 330 months is the correct answer