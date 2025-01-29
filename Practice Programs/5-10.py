current_users = ['may', 'thadar', 'kyaw', 'yoon', 'eaint']
new_users = ['MAY', 'mue', 'aung', 'yoon', 'eaint']

for user in new_users:
    if user in current_users:
        print(f"{user} needs to enter new username")
    else:
        print(f"{user} is available")