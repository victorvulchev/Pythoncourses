numb = int(input("insert a number between 0 and 999 -"))

ones = ["", "едно", "две", "три", "чертири", "пет", "шест", "седем", "осем", "девет"]
teens = ["", "единадесет", "дванадесет", "тринадесет", "четиринадесет", "петнадесет", "шестнадесет", "седемнадесет", "осемнадесет", "деветнадесет"]
tens = ["", "десет", "двайсет", "трийсет", "четиридесет", "петдесет", "шейсет", "седемдесет", "осемдесет", "деветдесет"]
hundreds = ["", "сто", "двеста", "триста", "четиристотин", "петстотин", "шестстотин", "седемстотин", "осемстотин", "деветстотин"]

start_Of_Number = int(numb // 100)
middle_Of_Number = int(numb % 100) // 10
end_Of_Number = int(numb % 10)

if numb == 0:
    print("нула")
elif numb == 10:
    print("десет")
elif numb >= 1 and numb <= 9:
    print(ones[numb])
elif numb >= 10 and numb <= 19:
    print(teens[end_Of_Number])
elif numb >= 20 and numb <= 99:
    end_Of_Number = int(numb % 10)
    start_Of_Number = int(numb // 10)
    if end_Of_Number == 0:
        print(tens[start_Of_Number])
    else:
        print(f"{tens[start_Of_Number]} и {ones[end_Of_Number]}")
else:
    if numb % 100 == 0:
        print(hundreds[start_Of_Number])
    elif end_Of_Number == 0:
        print(f"{hundreds[start_Of_Number]} и {tens[middle_Of_Number]}")
    elif middle_Of_Number < 2:
        print(f"{hundreds[start_Of_Number]} и {teens[middle_Of_Number]}")
    else:
        print(f"{hundreds[start_Of_Number]} {tens[middle_Of_Number]} и {ones[end_Of_Number]}")
        