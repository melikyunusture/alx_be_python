
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) 

celsius = " "

fahrenheit=" "

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32



tempinput = input ("Enter the temperature to convert:")
tempratureinputed = float (tempinput)


unitinput = input("is the temperature in celsius or Fahrenheit? type F for fehrenheit, C for celsius (C/F): ").upper() 

if unitinput == "F":
            
            celsius = convert_to_celsius(tempratureinputed)

           # print(f"{tempratureinputed}°F is {celsius}°C")

            print(tempratureinputed, "°F is", celsius, "°C" )

elif unitinput == "C":
            fahrenheit = convert_to_fahrenheit(tempratureinputed)
           # print(f"{tempratureinputed}°C is {fahrenheit}°F")

            print(tempratureinputed, "°c is", fahrenheit, "°F" )
else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")



