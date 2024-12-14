def make_album(name, title):
    """Create a dictionary containing album information."""
    myal = {
        'Artist': name.title(),       # Format artist's name to title case
        'Album Title': title.title()  # Format album title to title case
    }
    return myal

# While loop to collect user input
while True:
    print("\nPlease enter the album's artist and title:")
    print("(Type 'quit' at any time to stop)")

    # Get input from the user
    artist = input("Enter artist name: ")
    if artist.lower() == 'quit':   # Quit condition
        break
    
    title = input("Enter album title: ")
    if title.lower() == 'quit':    # Quit condition
        break

    # Call make_album() and print the resulting dictionary
    album = make_album(artist, title)
    print("\nHere's the album information:")
    print(album)
