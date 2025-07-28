    # Python 3 code to calculate Surface Area of a Cone
    # 'Hurray! Let's dive into the fun world of cones. Who said geometry can't be fun, eh?'

    import math # We need this little one to perform our calculations

    # This fun little function is going to do the actual work of computing the surface area of the cone
    def calculate_surface_area(radius, height):
        # Math time begins! Careful not to get too dizzy with the calculations
        base_area = math.pi * radius * radius # This will calculate the base area of our cone
        side_area = math.pi * radius * math.sqrt((radius ** 2) + (height ** 2)) # This calculates the side area of our cone
        total_area = base_area + side_area  # Add them up and VOILA! We have the surface area
        return total_area

    # And here is where we gather the measurements for our little cone friend
    def get_dimensions():
        # First thing we need is the radius of the base of the cone
        radius = float(input("Enter the radius of the Cone:"))

        # And let's not forget the height; without it, we just have a circle!
        height = float(input("Enter the height of the Cone:"))
        return radius, height 

    # Welcome to our main function! This is where all our fun code gets to run around and play
    def main():
        radius, height = get_dimensions()  # Get the radius and height by calling the function mentioned above
        total_area = calculate_surface_area(radius, height)  # Use the above to calculate the surface area with the little function we made
        print("Surface Area of the Cone is ", total_area, "unit square.")  # Look at that! You did it!

    # This is the final piece, where we say 'GO!'.
    # If this script is called, it's gonna run the main function, and all our magic will happen
    if __name__ == "__main__":
        main()
