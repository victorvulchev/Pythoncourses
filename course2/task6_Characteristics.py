def characteristic(input):
     first_Name = input[0]
     last_Name = input[1]
     age = input[2]
     gender = input[3]
     unique_Number = input[4]
     print("First Name: " + first_Name)
     print("Last Name: " + last_Name)
     print("Age: " + str(age))
     print("Gender: " + gender)
     print("Number: " + str(unique_Number))

characteristic(["Victor", "Valchev", 26, "m", 27560000])