class Admin:
    def __init__(self, fname, lname, email, phno):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phno = phno
        self.privileges = []  # Initialize privileges as an empty list
        
    def show_privileges(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        print("Privileges: " + ", ".join(self.privileges))  # Join the privileges list into a single string

# Create an instance of the Admin class
admin = Admin("John", "Doe", "john.doe@example.com", "1234567890")

# Show and print the privileges
admin.show_privileges()
