
def starting_coord_by_user():
    """Allows user to input their own coordinates for the starting point of a route

    Returns: list
    User-defined coordinates as a list.
    """
    print("Please enter your starting coordinates here:")
    lat = float(input("Enter latitude: "))
    long = float(input("Enter longitude: "))
    coordinates = [lat,long]
    print("Your starting coordinates: " + str(coordinates))
    
    return coordinates