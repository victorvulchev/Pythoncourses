age = int(input("age - "))
sex = input("sex - ")
married = input("married - ")

if sex == "F":
    print("Can only work in urban areas")
elif sex == "M" and (age >= 20 and age < 40):
    print("Can work anywhere")
elif sex == "M" and (age >= 40 and age <= 60):
    print("Can only work in urban areas")
else:
    print("error")
