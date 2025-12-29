
# Hello, beautiful people! Welcome to our fun-damental python script "WeatherCLIParser".
# This script parses a simple text file containing weather report and formats it in a way that's easy on the eyes!
# The best thing? It's all CLI, no internet, no dependencies, pure python!

# But hold on, you may wonder, why do this?
# Well, one could want to serve their grandparents a good weather forecast. 

# So, let's clasp our coding belts and dive into this digital adventure!!!
import os

def read_weather_report(file_path):
    """
    Let's read the weather report from a text file.
    All the gory details of the weather hiding in that .txt will be ours soon!
    """
    try:
        with open(file_path) as file:
            data = file.read()
    except Exception as e:
        print(f"Oops, seems like you got a tavern brawl with the text file\nDo check it and try again!\n{str(e)}")
        return None

    # Victory! We've safely slapped the data from our text file.
    return data

def format_weather_report(data):
    """
    Now it's time to make that raw, unprocessed data into something beautiful!
    Let's arrange weather data into a nicely formatted str.
    """
    try:
        # Let's tidy things up!
        formatted_data = "\n".join([f"{line.strip()}" for line in data.split("\n") if line.strip()])
    except Exception as e:
        print(f"Some hiccup in formatting! How did that happen!\n{str(e)}")
        return None
    
    # Tada! The data is now tidy and clean as a sphinx's nose (the nose is not there ;))
    return formatted_data

def main():
    # How exciting! Time to show off our python superpowers!
    # We're not dealing with any GUI here. It's all command line. A coder's best friend!
    print("\nWelcome to our Weather report CLI! May sunshine lead your path!")
    file_path = input("\nPlease enter path for your text weather report:\n")

    # Check if file path exists or not
    if not os.path.isfile(file_path):
        print("\nUnfortunately, the file path you entered leads nowhere! Please try again.\n")
        return
    # We've got the map, brute forcing our way into the mysterious text file.
    data = read_weather_report(file_path)
    
    # Got the lapidary data, let's polish it to jewellery now.
    if data is not None:
        formatted_data = format_weather_report(data)
        if formatted_data is not None:
            print("\nHere we go, set your eyes for a trimmed and cushioned weather report:\n")
            print(formatted_data)

if __name__ == "__main__":
    # Python gods, shower us your blessings from heavens!
    main()

