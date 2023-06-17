# The program will calculate a user’s holiday cost including the plane cost, hotel cost, and car rental cost.


# Welcome message
print ("Welcome to holiday cost plan")

# Asking for the city they will be flying to
# To eliminate any error by user input list valid_city is created and continue with while loop
# Using while loop with if statement errors will be eliminate
valid_city = ["london", "barcelona", "dubai", "cairo", "amsterdam"]
print("Choose from the list below a city you want to go on holiday: ")
while True:
    print("London, Barcelona, Dubai, Cairo, Amsterdam.")
    city_flight = (input("Enter the city name: ")) 
    if city_flight.lower() in valid_city:
        break
    else:
        print("Invalid city! ")

# Asking for the number of nights they will be staying at a hotel
# Use while loop with try and except to eliminate any error enter by the user
while True:
    try:
        num_nights = int(input("How many night do you have your hotel accommodation for? "))
        break
    except ValueError:
        print("Invalid value, please enter a number! ")

# Asking for the number of days that they will be hiring a car
# Use while loop with try and except to eliminate any error enter by the user
while True:
    try:
        rental_days = int(input("How many day are you going to rent a car? "))
        break
    except ValueError:
        print("Invalid value, please enter a number! ")

# Create hotel_cost function
# This function will take the num_nights as an argument, and return a total cost for the hotel stay
def hotel_cost(num_nights):
    return 10 * num_nights
    
# Create plane_cost function
# This function will take the city_flight as an argument and return a cost for the flight 
# Use if/else if statements in the function to retrieve a price based on the chosen city
def plane_cost(city_flight):
    if city_flight.lower() == "london":
        return 300
    elif city_flight.lower() == "barcelona":
        return 400
    elif city_flight.lower() == "dubai":
        return 600
    elif city_flight.lower() == "cairo":
        return 600
    elif city_flight.lower() == "amsterdam":
        return 350
    else:
        return 0

# Create car_rental function
# This function will take the rental_days as an argument and return the total cost of the car rental
# calculate daily rental cost * number of days
def car_rental(rental_days):
    return 15 * rental_days

# Create holiday_cost function
# This function will take the three arguments hotel_cost, plane_cost, car_rental. 
# Using these three arguments, call all three of the above functions with respective arguments
# Finally return a total cost for your holiday.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# Change the name city to capital letters to be more visible in the results
city_flight = city_flight.upper()


# Print out all the details about the holiday
print(f"\nTotal cost of your holiday to {city_flight} is:")
print(f"\nThe flight cost is £ {plane_cost(city_flight)}")
print(f"The total cost to rent a car is £ {car_rental(rental_days)}.")
print(f"The total cost for accommodation is £ {hotel_cost(num_nights)}.")
print(f"The total cost of your holiday is £ {holiday_cost(hotel_cost, plane_cost, car_rental)}")
