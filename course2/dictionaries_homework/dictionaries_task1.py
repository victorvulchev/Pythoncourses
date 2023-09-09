numb = int(input("insert a number between 0 and 999 -"))

translations = { "ones" : ["", "едно", "две", "три", "чертири", "пет", "шест", "седем", "осем", "девет"],
"teens" : ["", "единадесет", "дванадесет", "тринадесет", "четиринадесет", "петнадесет", "шестнадесет", "седемнадесет", "осемнадесет", "деветнадесет"],
"tens" : ["", "десет", "двайсет", "трийсет", "четиридесет", "петдесет", "шейсет", "седемдесет", "осемдесет", "деветдесет"],
"hundreds" : ["", "сто", "двеста", "триста", "четиристотин", "петстотин", "шестстотин", "седемстотин", "осемстотин", "деветстотин"]}

start_Of_Number = int(numb // 100)
middle_Of_Number = int(numb % 100) // 10
end_Of_Number = int(numb % 10)

if numb == 0:
    print("нула")
elif numb == 10:
    print("десет")
elif numb >= 1 and numb <= 9:
    print(translations["ones"][numb])
elif numb >= 10 and numb <= 19:
    print(translations["teens"][end_Of_Number])
elif numb >= 20 and numb <= 99:
    end_Of_Number = int(numb % 10)
    start_Of_Number = int(numb // 10)
    if end_Of_Number == 0:
        print(translations["tens"][start_Of_Number])
    else:
        print(f'{translations["tens"][start_Of_Number]} и {translations["ones"][end_Of_Number]}')
else:
    if numb % 100 == 0:
        print(translations["hundreds"][start_Of_Number])
    elif end_Of_Number == 0:
        print(f'{translations["hundreds"][start_Of_Number]} и {translations["tens"][middle_Of_Number]}')
    elif middle_Of_Number < 2:
        print(f'{translations["hundreds"][start_Of_Number]} и {translations["teens"][middle_Of_Number]}')
    else:
        print(f'{translations["hundreds"][start_Of_Number]} {translations["tens"][middle_Of_Number]} и {translations["ones"][end_Of_Number]}')