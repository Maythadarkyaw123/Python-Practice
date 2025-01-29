sandwich_orders = ['mysandwich','yoursandwich','theirsandwich']
finished_sandwiches = []

for order in sandwich_orders:
    print(f'Thanks for buying {order}')
    finished_sandwiches.append(order)
print(f'Here are finished sandwiches {finished_sandwiches}')