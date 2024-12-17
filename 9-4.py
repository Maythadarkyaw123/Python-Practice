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

# Create an instance of the Restaurant class
restaurant = Restaurant("heyhey", "soup")
restaurant.describe_restaurant()

# Setting the number of customers served
restaurant.set_number_served(200)

# Incrementing the number of customers served
restaurant.increment_number_served(50)
