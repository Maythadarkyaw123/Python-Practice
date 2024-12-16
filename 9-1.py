class Restaurant(): #class starting
    def __init__(self, restaurant_name, cuisine_type): #__init__ is constructor, self is instance of class itself
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Restaurant Name: " + self.restaurant_name)
        print("Restaurant Type: " + self.cuisine_type)# first original function with its attribute and other whatever you want to call

restaurant = Restaurant("heyhey", "soup")
restaurant.describe_restaurant()

  



