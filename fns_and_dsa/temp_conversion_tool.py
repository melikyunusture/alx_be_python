
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


tempinput = input ("Enter the temperature to convert:")
tempratureinputed = float (tempinput)


unitinput = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper() 

if unitinput == "F":
            
            celsius = convert_to_celsius(tempratureinputed)

            print(tempratureinputed, "°F is", celsius, "°C" )

elif unitinput == "C":
            fahrenheit = convert_to_fahrenheit(tempratureinputed)
            print(tempratureinputed, "°c is", fahrenheit, "°F" )
else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")



