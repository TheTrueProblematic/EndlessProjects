
# TemperatureChart.py

# Welcome to Temperature Chart program! Put your coat on (or take it off), 
# because we're about to go on a journey through Celsius, Fahrenheit and Kelvin!
# This is a chill little script with no dependencies or internet requirements, 
# so you can run it wherever you like, even at the North or South Pole!

def celsius_to_fahrenheit(celsius):
    # Turns the Celsius temp to Fahrenheit, because some like it hot!
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    # Turns the Celsius temp to Kelvin, for those of us doing science in absolute zero conditions!
    return celsius + 273.15

def celsius_chart(start, end):
    # Draws a temperature conversion chart from start to end (Celsius)
    print("Celsius\tFahrenheit\tKelvin")
    for i in range(start, end+1):
        print(f"{i}\t{celsius_to_fahrenheit(i)}\t\t{celsius_to_kelvin(i)}")

if __name__ == '__main__':
    # Default range from -100 to 100 degrees Celsius. Adjust to fit your personal climate preferences!
    print("Temperature Chart from -100 to 100 degrees Celsius:\n")
    celsius_chart(-100, 100)

# Thanks for joining this temperature conversion chart adventure! Stay cool, or warm, or whatever you prefer!!!

