class User:
    def __init__(self, first_name, last_name, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.login_attempts = 0  # Add login_attempts attribute with a default value of 0

    def describe_user(self):
        print(f"First name is {self.first_name} and last name is {self.last_name} and email is {self.email} and phone number is {self.phone_no}")

    def greet_user(self):
        print("Hey, nice to meet you!")
        print("--------------------------------")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create instances of the User class
first_user = User("May", "Kyaw", "may@gmail.com", 123)
second_user = User("May", "Thadar", "thadar@gmail.com", 456)
third_user = User("Thadar", "Kyaw", "kyaw@gmail.com", 789)

# Describe and greet users
first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()

third_user.describe_user()
third_user.greet_user()

# Increment login attempts
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(f"Login attempts for first_user: {first_user.login_attempts}")

second_user.increment_login_attempts()
print(f"Login attempts for second_user: {second_user.login_attempts}")

third_user.increment_login_attempts()
third_user.increment_login_attempts()
print(f"Login attempts for third_user: {third_user.login_attempts}")

# Reset login attempts
first_user.reset_login_attempts()
print(f"Login attempts for first_user after reset: {first_user.login_attempts}")

second_user.reset_login_attempts()
print(f"Login attempts for second_user after reset: {second_user.login_attempts}")

third_user.reset_login_attempts()
print(f"Login attempts for third_user after reset: {third_user.login_attempts}")
