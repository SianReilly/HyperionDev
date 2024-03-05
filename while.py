# ========= Task 1 ===========
# Creating an empty list to store all numbers:
numbers= []

# This while loop continually requests the user to enter a real number (can contain a decimal; a float).
# The while loop breaks at -1 and includes a ValueError (inbuilt python exception) if there is an invalid input.
while True:
    try:
        user_number = float(input("Please enter a number (enter -1 to exit the loop):"))
        if user_number == -1:
            break
        numbers.append(user_number)

    except ValueError:
        print("There is an invalid input entered- please enter a number.")

# The while loop then calculates the average of the numbers, rounded to 2 decimal points for readability.
# If no numbers were entered, e.g. 'hello', then the output states no numbers were entered.
    if numbers:
        average = sum(numbers)/len(numbers)
        print(f"The average of the numbers entered is: {average:.2f}")
    else:
        print("No numbers were entered.")


""" 
NOTES:
len() returns the length of an object.
.append adds an item to the end of a list.
There are a lot of built in exceptions, maybe a TypeError would be preferable here over a ValueError.
The TypeError could indicate it has to be a float?- https://docs.python.org/3/library/exceptions.html
"""
