budget = float(input())
category = input()
people = float(input())
transport = 0
ticket = 0

if people <= 4:
    transport += budget * 0.75
elif people <= 9:
    transport += budget * 0.6
elif people <= 24:
    transport += budget * 0.5
elif people <= 49:
    transport += budget * 0.4
else:
    transport += budget * 0.25

if category == "VIP":
    ticket = 499.99
else:
    ticket = 249.99

cost_Per_Person = people * ticket
total_Cost = transport + cost_Per_Person
diff = abs(budget - total_Cost)

if budget >= total_Cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")