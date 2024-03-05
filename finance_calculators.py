# ========= Task 1 ===========
# Defining via functions the two types of calcuation for the user: investment or bond.

# If the user inputs 'investment', the deposit amount, interest rate, number of investment years and interest type will determine the final investment amount. The final amount is rounded up to two decimal places for readability.

# If the user inputs 'bond', the present house value, interest rate and number of repayment months will determine the monthly repayment amount. The monthly repayment amount is rounded up to two decimal places for readability. 


# Importing all the relevant modules:
import math

# Defining the two calculator functions: 'investment' and 'bond'
def calculate_investment(deposit_amount, rate, investment_years, interest_type):
    if interest_type.lower() == "simple":
        return deposit_amount * (1 + rate/100 * investment_years)
    elif interest_type.lower() == "compound":
        return deposit_amount * math.pow((1+rate/100),investment_years)

def calculate_bond(present_house_value, interest_rate, number_of_months):
    monthly_interest_rate = interest_rate/1200
    monthly_payment = (monthly_interest_rate * present_house_value) / ((1-(1 + monthly_interest_rate) ** (- number_of_months)))
    return monthly_payment

# Guiding the user input:
print(" investment - to calculate the amount of interest you'll earn on your investment")
print(" bond - to calculate the amount you'll have to pay on a home loan")
print(" Enter either 'investment' or 'bond' from the menu above to proceed:")

user_choice = input("Enter your choice:").lower()

# Calling investment function and calculating as per user input:
if user_choice == "investment":
    deposit_amount = float(input("Please enter your deposit amount for investment:"))
    rate = float(input("Please enter the interest rate as an integer:"))
    investment_years = float(input("Please enter the number of years you plan to invest for:"))
    interest_type = input("Please select by typing out your chosen interest type: 'simple' or 'compound'")
    final_amount = calculate_investment(deposit_amount, rate, investment_years, interest_type)
    format_final_amount = "{:.2f}".format(final_amount)
    print(f"Over your given period of {investment_years} years at the specified interest rate of {rate}%, you will receive the final amount of {format_final_amount} in your currency.")

# Calling bond function and calculating as per user input:
if user_choice == "bond":
    present_house_value = float(input("Please enter the present value of the house:"))
    interest_rate = float(input("Please enter the interest rate as an integer:"))
    number_of_months = float(input("Please enter the number of months you plan to take to repay the bond:"))
    final_amount = calculate_bond(present_house_value, interest_rate, number_of_months)
    format_final_amount = "{:.2f}".format(final_amount)
    print(f"Over your given period of {number_of_months} months at the specified interest rate of {interest_rate}%, you will have to repay {format_final_amount} each month for your home loan in your currency.")



""" 
NOTES:
.lower ensures that the input will be lowercase regardless of user input.
math.pow returns the value of the deposit amount raised to a power (import math module) 
"""
