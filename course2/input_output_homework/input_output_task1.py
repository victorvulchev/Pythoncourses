numb = str(input())
new_numb1 = numb[0] + numb[3]
new_numb2 = numb[1] + numb[2]

if int(new_numb1) > int(new_numb2):
    print(f"{new_numb1}>{new_numb2}")
elif int(new_numb1) == int(new_numb2):
    print(f"{new_numb1}={new_numb2}")
else:
    print(f"{new_numb1}<{new_numb2}")