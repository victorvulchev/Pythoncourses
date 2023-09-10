rain = {}
command = input("Enter City:")

while command != "":
    city = command
    command = int(input("Enter rain:"))
    temp_rain = command
    total_rain = 0
    if city not in rain:
        rain[city] = temp_rain
    else:
        total_rain = rain.get(city) + temp_rain
        rain[city] = total_rain
    command = input("Enter City:")

for key, value in rain.items():
    print(f"{key}: {value}")

