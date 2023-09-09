numb = input()

if "0" in str(numb):
    print("Number includes a 0")
else:
    a = str(numb[0])
    b = str(numb[1])
    c = str(numb[2])
    
    if int(numb) % int(a) == 0 and int(numb) % int(b) == 0 and int(numb) % int(c) == 0:
        print(f"{a}:{b}:{c} can be devided")
    else:
        print("Cannot devide with every number")