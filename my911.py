# user.py

class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.user_info.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()
