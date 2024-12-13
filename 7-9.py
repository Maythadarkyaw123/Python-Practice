sandwich_orders = ['mysandwich','yoursandwich','theirsandwich','pastrami', 'pastrami','pastrami']
finished_sandwich = []

print("The deli has run out of pastrami.🥲")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current = sandwich_orders.pop(0)
    finished_sandwich.append(current)
    
print(f'Sandwiches made: {finished_sandwich}')
