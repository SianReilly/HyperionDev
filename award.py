# ========= Task 1 ===========
# Task: Design a program that determines award a person receives after completing in a triathlon
# Read in times (mins) for all three events: swimming, cycling, running
# Calculate and display the total time taken to complete the triathlon
# Award receved is based on total time taken to complete the triathlon
# Qualifying time for awards is 100 minutes
# Display the award the participant will receive based on critieria

# Pseudocode:
# swimming_time = int(input("Please enter your swimming race time in minutes).")) 
# cycling_time = int(input("Please enter your cycling race time in minutes).")) 
# running_time = int(input("Please enter your running race time in minutes).")) 
# total_time = (swimming_time + cycling_time + running_time)
# print(f"The participants' total triathlon race time is {total_time}")

# If participant's total_time is >=0 and <=100 mins = print("The participant has been awarded Provincial Colours")
# Elif participant's total_time is >=101 and <=105 mins = print("The participant has been awarded Provincial Half Colours")
# Elif participant's total_time is >=106 and <=110 mins = print("The participant has been awarded Provincial Scroll")
# Else participant's total_time is >110 mins = print("The participant has no award")

# Practical Task 1:
# Assigning the variables, casting them into integers for the calculation
swimming_time = int(input("Please enter your swimming race time in minutes)."))
cycling_time = int(input("Please enter your cycling race time in minutes)."))
running_time = int(input("Please enter your running race time in minutes)."))

swimming_injury = bool(input("Do you have a swimming injury? Please enter 'True' or 'False'.)."))
cycling_injury = bool(input("Do you have a cycling injury? Please enter 'True' or 'False')."))
running_injury = bool(input("Do you have a running injury? Please enter 'True' or 'False')."))

nationality = str(input("""Please enter which region you represent from this list in order to be assigned the correct interview: 
                        England, Northern Ireland, Republic of Ireland, Scotland or Wales)."""))


# Calculating the total participant triathlon time
total_time = (swimming_time + cycling_time + running_time)

# Displaying the total participant triathlon time using an f string
print(f"The participants' total triathlon race time is {total_time}")


# Creating an if-elif-else statement to determine the partipant's award
# The if-elif-else statement uses both comparison (<=, >=) and logical conjunction (and) operators
if total_time >=0 and total_time <=100:
    print("The participant has been awarded Provincial Colours")
    # Draw a star image if awarded Provincial Colours
    print("   *   ")
    print(" *   * ")
    print("*******")
    print(" *   * ")
    print("   *   ")
elif total_time >=101 and total_time <=105:
    print("The participant has been awarded Provincial Half Colours")
elif total_time >=106 and total_time <=110:
    print("The participant has been awarded Provincial Scroll")
else:
    print("The participant has no award")


if swimming_injury and cycling_injury and running_injury:
    print("Please see Nick Murch, Richard Freeman, and  George A. Sheehan for treatment.")

elif swimming_injury and cycling_injury:
    print("Please see Nick Murch and Richard Freeman for treatment.")
elif swimming_injury and running_injury:
    print("Please see Nick Murch and Richard Freeman for treatment.")
elif running_injury and cycling_injury:
    print("Please see George A. Sheehan and Richard Freeman for treatment.")
    
elif cycling_injury:
    print("Please see Richard Freeman for treatment")
elif running_injury:
    print("Please see George A. Sheehan for treatment")
elif swimming_injury:
    print("Please see Nick Murch for treatment")

else:
    print("You do not require any treatment! Onto the next race :)")


if nationality == "England":
    print("Please attend the BBC interview at 4pm on the 11th May.")
elif nationality == "Northern Ireland":
    print("Please attend the UTV interview at 1pm on the 11th May.")
elif nationality == "Republic of Ireland":
    print("Please attend the RTÉ One interview at 2pm on the 11th May.")
elif nationality == "Wales":
    print("Please attend the BBC Cymru Wales interview at 11am on the 11th May.")
elif nationality == "Scotland":
    print("Please attend the STV interview at 10am on the 11th May.")
else:
    print("You entered an invalid response, please repeat the question.")