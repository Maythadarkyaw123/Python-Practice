
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)
        print("Customers Served: " + str(self.number_served))

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("Number of customers served has been set to: " + str(self.number_served))

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
        print(f"Incremented the number of customers served by {additional_customers}. Total now: {self.number_served}")
        
class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        self.flavors = flavors
        print("Flavor is:" + flavors)
        
    
        
IceCreamStand("Vanilla")
