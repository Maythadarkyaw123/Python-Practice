class Restaurant(): #class starting
    def __init__(self, restaurant_name, cuisine_type, dessert): #__init__ is constructor, self is instance of class itself
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.dessert = dessert
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Dessert: {self.dessert}")
        
Restaurant("Heyhey","soup","ice_cream").describe_restaurant()