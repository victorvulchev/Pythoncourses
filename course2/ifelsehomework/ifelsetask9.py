temperature_type = input("write c or f")
degrees = int(input())

if temperature_type == "c":
    celsius = degrees
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C is {fahrenheit} in Fahrenheit")
else:
    fahrenheit = degrees
    celsius = fahrenheit - 32 * 5 / 9
    print(f"{fahrenheit}°F is {celsius} in Celsius")
