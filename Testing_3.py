# What happens if we want to test multiple conditions? This is where elif comes in.

# num = int(input("Please input a number between 1 and 100"))

# if num < 12:
#     print("The value you entered is lower than 12")
# elif num > 18:
#     print("The value you entered is higher than 18")
# elif num < 16:
#     print("The value you entered is lower than 16")
# else:
#     print(f"The value you entered is {num}")


# current_time = 11
# if current_time < 11:
#     print("Time for a short jog – let’s go!")
# elif current_time == 11:
#     print("Can do a quick home workout instead.")
# else:
#     print("It’s after 11 – it’s lunch time.")

hour = int(input("Please input the hour as an integer from 1 to 24"))

if hour < 18:
    print("Good day")
elif hour < 20:
    print("Good evening")
else:
    print("Good night")
