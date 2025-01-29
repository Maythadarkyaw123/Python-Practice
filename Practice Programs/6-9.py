favorite_places = {
    "Alice": ["New York", "Los Angeles"],
    "Bob": ["Paris", "Berlin"],
    "Charlie": ["Tokyo", "Sydney"]
}

for key, value in favorite_places.items():
    print(f"{key}'s favorite places are:")
    for place in value:
        print(f"- {place}")
    print("-------------------------")