cars = 100   # Number of cars available.
space_in_a_car = 4.0  #Space of each car.
drivers = 30    #Number of drivers.
passengers = 90  #Number of passangers.
cars_not_driven = cars - drivers  #Cars not driven due to lack of drivers.
car_driven = drivers  #Number of driven cars.
carpool_capacity = car_driven * space_in_a_car # Total capacity of carpooling.
average_passengers_per_car = passengers /  car_driven # Average person per car.


print("There are", cars,"cars available.") #to print available car.
print("There are only",drivers,"drivers available.") #to print available drivers.
print("There will be ",cars_not_driven,"empty cars today.") #to print number of cars not driven.
print("We can transport", carpool_capacity,"people today.") # to print carpoool capacity.
print("We have",passengers,"to carpool today.") #to print number of passengers .
print("We need to put about",average_passengers_per_car,"in each car.") #to print average person per car.