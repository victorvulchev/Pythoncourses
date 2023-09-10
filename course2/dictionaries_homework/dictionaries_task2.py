age = int(input("Age:"))
sex = input("Sex:")
height = int(input("Height:"))
weight = float(input("Weight:"))
activity = int(input("Physical activity 1-6:"))
person = {}
person["Age"] = age
person["Sex"] = sex
person["Height"] = height
person["Weight"] = weight
person["Activity"] = activity
print(person)

bmr = 0
if sex == "m":
    bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
else:
    bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

actual_bmr = 0
if activity == 1 or activity == 2 or activity == 3:
    actual_bmr = bmr * (1.2 * bmr) * 1.375
elif activity == 4:
    actual_bmr = bmr * 1.55
elif activity == 5:
    actual_bmr = bmr * 1.725 
else:
    actual_bmr = bmr * 1.9

goals = {}
maintain = actual_bmr
lose_500 = actual_bmr - 500
lose_1 = actual_bmr - 1000
gain_500 = actual_bmr + 500
gain_1 = actual_bmr + 1000
goals["Maintain Weight"] = f"Имате нужда от {round(maintain)} Калории на ден за да поддържате теглото си"
goals["Lose 0.5kg"] = f"Имате нужда от {round(lose_500)} Калории на ден за да сваляте по 0.5 кг на седмица"
goals["Lose 1kg"] = f"Имате нужда от {round(lose_1)} Калории на ден за да сваляте по 1 кг на седмица"
goals["Gain 0.5kg"] = f"Имате нужда от {round(gain_500)} Калории на ден за да качвате по 0.5 кг на седмица"
goals["Gain 1kg"] = f"Имате нужда от {round(gain_1)} Калории на ден за да качвате по 1 кг на седмица"

for val in goals.values():
    print(val)