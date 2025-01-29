favnum = {
    "May": [1,2],
    "Thadar": [3,4],
    "Kyaw": [5,6],
    "Yoon Yoon": [7,8],
    "Eaint" : [9,10]
}

for key, value in favnum.items():
    print(f"{key}'s favorite number are:")
    for num in value:
        print(f'{num}')