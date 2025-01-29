class User():
    def __init__(self, first_name, last_name, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        
    def describe_user(self):
        print(f"First name is {self.first_name} and last name is {self.last_name} and email is {self.email} and phone number is {self.phone_no}")
        
    def greet_user(self):
        print("Hey Nice to meet you!")
        print("--------------------------------")

first_user = User("May", "Kyaw", "may@gmail.com", 123)    
first_user.describe_user()   
first_user.greet_user()

second_user = User("May", "Thadar", "thadar@gmail.com", 456)
third_user = User("Thadar", "Kyaw", "kyaw@gmail.com", 789)

second_user.describe_user()   
second_user.greet_user()

third_user.describe_user()   
third_user.greet_user()


        