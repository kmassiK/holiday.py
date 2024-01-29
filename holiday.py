# Programming with User_defined Function - Practical task

# We're tasked to create a program to calculate a user's total holiday cost.
# which includes plane cost, hotel cost and car rental cost.


# Choice of destinations available
print("\nList of available destinations: \nAbidjan \nNairobi \nConakry \nKigali")

# Create a list of cities, price of the flight, hotel price and car rental price.
city_list = ['Abidjan', 'Nairobi', 'Conakry', 'Kigali']
flight_price_list = [800, 1000, 850, 900]
price_hotel_list = [200, 300, 100, 280]
car_rental_list = [90, 100, 70, 80] 

# create  dictionaries to store flight, hotel and car rentals price per city
city_flight_dict = {key: value for key, value in zip(city_list, flight_price_list)}
print("\nCost of flight per destination:")
print('\n'.join("{}: {}".format(k, v) for k, v in city_flight_dict.items()))

city_hotel_dict = {key: value for key, value in zip(city_list, price_hotel_list)}
print("\nHotel price per night per destination:")
print('\n'.join("{}: {}".format(k, v) for k, v in city_hotel_dict.items()))

city_car_dict = {key: value for key, value in zip(city_list, car_rental_list)}
print("\nCar rental price per day per destination:")
print('\n'.join("{}: {}".format(k, v) for k, v in city_car_dict.items()))

# Choosing the destination
while True:
    city_flight = input("\nEnter the city you're flying to from the list above: ").capitalize()
    if city_flight.isnumeric():
        print("Error, this is a number, please enter a city from the available destination.")
        continue
    elif city_flight not in city_list:
        print("Invalid entry, please choose from the list above.")
        continue
    else:
        break

 # getting the nember of night stay at the hotel.               
while True:
    try:
        num_nights = int(input("\nEnter the number of nights you're planning to stay: "))
    except:
        print("Please enter a valid number: ")
    else:
        print(f"You've entered {num_nights}.")
        break

# Getting the number of days with the rental car
while True:
    try:
        rental_days = int(input("\nEnter the number of days you will rent a car for: "))
    except:
        print("Please enter a valid number: ")
    else:
        print(f"You've entered {rental_days}.")
        break  

def hotel_cost(num):
    '''Calculate the total cost for the hotel stay
    and takes the number of nights as argument'''
    if city_flight == 'Abidjan':
       return city_hotel_dict['Abidjan'] * num_nights
    elif city_flight == 'Nairobi':
        return city_hotel_dict['Nairobi'] * num_nights
    elif city_flight == 'Conakry':
       return city_hotel_dict['Conakry'] * num_nights
    elif city_flight == 'Kigali':
        return city_hotel_dict['Kigali'] * num_nights
    
  
def plane_cost(city):
    '''Calculate the cost of the flight, 
    takes city flight as argument'''
    if city_flight == 'Abidjan':
       cost_of_flight = city_flight_dict['Abidjan'] 
       return cost_of_flight
    elif city_flight == 'Nairobi':
        cost_of_flight = city_flight_dict['Nairobi'] 
        return cost_of_flight
    elif city_flight == 'Conakry':
       cost_of_flight = city_flight_dict['Conakry'] 
       return cost_of_flight
    elif city_flight == 'Kigali':
        cost_of_flight = city_flight_dict['Kigali'] 
        return cost_of_flight
    

def car_rental(num):
    '''Calculate the cost for the rental car, 
    takes rental days as argument'''
    if city_flight == 'Abidjan':
       return city_car_dict['Abidjan'] * rental_days
    elif city_flight == 'Nairobi':
        return city_car_dict['Nairobi'] * rental_days
    elif city_flight == 'Conakry':
       return city_car_dict['Conakry'] * rental_days
    elif city_flight == 'Kigali':
        return city_car_dict['Kigali'] * rental_days
     
    
def holiday_cost(cost_1, cost_2, cost_3):
    '''Calculate the total cost of the holiday by adding the flight, hotel
    and car rental cost together'''
    total = sum([cost_1, cost_2, cost_3])
    return total

print(f"\nThe total Hotel Cost is £{hotel_cost(num_nights)}")
print(f"\nThe total flight Cost is £{plane_cost(city_flight)} per person") 
print(f"\nThe total car rental Cost is £{car_rental(rental_days)}") 
total_holiday_cost = holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))
print(f"\nThe total cost of your holiday is: £{total_holiday_cost}\n")