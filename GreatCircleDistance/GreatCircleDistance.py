
# Hello, fellow Python lovers! 
# Our task today is to calculate the Great Circle Distance between two points on a spherical Earth, 
# because let's face it, we've all wondered if we could calculate the distance between two GPS coordinates. Who needs google maps, right?

import math

def get_rad(degree_val):
    """Converts the degree value to radians as trigonometric functions use radians not degrees"""
    return math.radians(degree_val)

def get_great_circle_distance(lat1, lon1, lat2, lon2):
    """Calculates the Great Circle Distance between two lat/long points on the surface of Earth"""
    
    # Step 1: Convert latitudes and longitudes to spherical coordinates in radians.
    # Latitude values are mapped from -90 to +90 degrees to 0 to Pi radians.
    # Longitude values are mapped from -180 to +180 degrees to 0 to 2Pi radians.
    lon1, lat1, lon2, lat2 = map(get_rad, [lon1, lat1, lon2, lat2])
    
    # Step 2: Use the Haversine formula to get the distance in radians between lat1 and long1
    # The Haversine formula: Hav(distance) = Hav(lat2 - lat1) + cos(lat1) * cos(lat2) * Hav(long2 - long1)
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    a_value = (math.sin(delta_lat / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * (math.sin(delta_lon / 2) ** 2)
    
    # Convert the distance in radians to the actual distance using the radius of the Earth (Assumed to be spherical)
    # Earth's radius varies between 6,378 km - 6,357 km => Taking the average radius as 6,371 km or approximately 3961 miles
    earth_radius_km = 6371
    c_value = 2 * math.atan2(math.sqrt(a_value), math.sqrt(1 - a_value))
    great_circle_distance = earth_radius_km * c_value
    
    return great_circle_distance

# Driver Code to test the function
if __name__ == "__main__":
    # Get user input for the coordinates
    lat1 = float(input("Enter Latitude 1: "))
    lon1 = float(input("Enter Longitude 1: "))
    lat2 = float(input("Enter Latitude 2: "))
    lon2 = float(input("Enter Longitude 2: "))
    
    # Call the Great Circle Distance function
    gcd = get_great_circle_distance(lat1, lon1, lat2, lon2)
    
    # Display the result
    print(f"The Great Circle Distance between ({lat1}, {lon1}) and ({lat2}, {lon2}) is {gcd} kms!")

# What a joy to program in python! Job done!

