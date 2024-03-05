# ========= Task 1 ===========
# Writing a program to calculate a user's total holiday cost = plane, hotel and car-rental cost


# Creating the four functions to calculate each cost and the overall holiday cost:

# Hotel Cost - takes the number of nights as an argument and returns the total hotel stay cost.
def hotel_cost(num_nights):
    nightly_rate = 45
    return num_nights * nightly_rate


# Plane Cost - takes the city_flight as an argument and keeps the city: city_flight_cost in a dictionary.
def plane_cost(city_flight):
    flight_costs ={
        'Berlin': 250,
        'Malaga': 350,
        'New Zealand': 1000,
        'Dublin': 35,
    }
    return flight_costs.get(city_flight, "City is not in the flight list.")

# Car rental - takes the rental_days as an argument and returns the car rental cost total.
def car_rental(rental_days):
    daily_rate = 20
    return rental_days * daily_rate

# Holiday Cost - takes all the previous functions to add the hotel, plane and car costs together.
def holiday_cost(num_nights,city_flight,rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + flight + car
    return total_cost

# Asking the user for inputs:
print("Here are the available flight destinations with associated costs:")
print("Berlin: £250, Malaga: £350, New Zealand: £1000, Dublin: £35")


# Getting the following user inputs for the holiday:
city_flight = input("Please enter the city you will be flying to:")
num_nights = int(input("Please enter the number of nights you will stay at the hotel:"))
rental_days = int(input("Please enter the number of days that you will rent a car:"))


# Creating the hotel, flight and car prices by calling the above functions:
hotel_price = hotel_cost(num_nights)
flight_price = plane_cost(city_flight)
car_price = car_rental(rental_days)
total_holiday_price = holiday_cost(num_nights, city_flight,rental_days)


# Printing out all holiday details in a readable way:
print("\nHere is the breakdown of your holiday costs:")
print(f"\n The total hotel cost for {num_nights} nights is £{hotel_price}")
print(f"\n The plane ticket for {city_flight} costs £{flight_price}")
print(f"\n The car rental for {rental_days} days costs £{car_price}")

