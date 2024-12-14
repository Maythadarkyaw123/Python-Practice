# Original list of magicians
magicians = ['mg', 'hnin', 'thu']

# Function to display magicians
def show_magicians(magician_list):
    """Print each magician's name in uppercase."""
    for magician in magician_list:
        print(magician.upper())

# Function to add 'the Great' to each magician's name
def make_great(magician_list):
    """Add 'the Great' to each magician's name and return a new list."""
    great_magicians = []  # Create an empty list for modified names
    for magician in magician_list:
        great_magicians.append(magician.title() + " the Great")
    return great_magicians

# Create a new list with 'the Great' added to each name
great_magicians_list = make_great(magicians)

# Show the original list of magicians
print("\nOriginal List of Magicians:")
show_magicians(magicians)

# Show the new list with 'the Great' added
print("\nList of Great Magicians:")
show_magicians(great_magicians_list)
