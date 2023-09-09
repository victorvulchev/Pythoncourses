temperature = int(input())

if temperature <= -20:
    print("ледено")
elif temperature > -20 and temperature <= 0:
    print("студено")
elif temperature > 0 and temperature <= 15:
    print("хладно")
elif temperature > 15 and temperature <= 25:
    print("топло")
else:
    print("горещо")