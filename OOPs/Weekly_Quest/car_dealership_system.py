# Project : Developing a Car Dealership Inventory System 
#     • Description: Explore class relationships by building a car dealership inventory system.
#                    Define classes for cars, dealerships, and customers. 
#                    Include methods for adding cars to inventory, displaying available cars, and simulating customer purchases. 
#     • Tasks: 
#                 o Design classes for cars, dealerships, and customers. 
#                 o Implement methods for managing inventory and handling customer transactions. 
#                 o Test the system with various car additions and customer interactions. 

class Car:
    def __init__(self, car_maker, car_name, car_model, car_manufacturing_year, car_price):
        self.car_maker = car_maker
        self.car_name = car_name
        self.car_model = car_model
        self.car_manufacturing_year = car_manufacturing_year
        self.car_price = car_price

    def  display_details(self):
        print('Car Maker : ',self.car_maker)
        print('Car Name : ', self.car_name)
        print('Car Model : ', self.car_model)
        print('Car Manufacturing Year : ', self.car_manufacturing_year)
        print('Car Price : ', self.car_price)

class DealerShip():
    def __init__(self, name):
        self.name= name
        self.inventory = []

    def add_to_inventory(self, new_car):
        self.inventory.append = new_car
    
    def available_car (self, name):
        if self.name in self.inventory:
            return f'{self.name} is  currently available.'
        else:
            return 'This car is not available at this time.'

        
class Customer:
    def __init__(self, first_name, last_name, customer_id, address, car_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_id = customer_id
        self.address = address
        self.car_name = car_name

        self.purchased_car = []

    def purchased_car_(self, bought_car):
        self.purchased_car.append(bought_car)


car1 = Car('Pagani', 'Huayra', 'M8', 2017, 80000000)
car2 = Car('Roll Royals', 'Phantom', 2022, 600000000)
car3 = Car('Porchse', '911', '911', 2012, 221400000)
car4 = Car('Cadillac', 'Moris', '61', 1961, 6400000)
