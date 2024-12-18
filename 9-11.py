# main.py

from my911 import Admin

admin_user = Admin('Alice', 'Smith', title='Admin', email='alice@example.com')
admin_user.privileges.show_privileges()
