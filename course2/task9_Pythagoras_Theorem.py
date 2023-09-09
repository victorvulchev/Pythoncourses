def pythagoras_Theorem(input):
     a = int(input[0])
     b = int(input[1]) 
     c = int(input[2])
     pow_A = a ** 2
     pow_B = b ** 2
     pow_C = c ** 2

     if pow_A + pow_B == pow_C:
          toPrint = f"{a}^2 + {b}^2 = {c}^2"
          print(toPrint)
     else:
          print("Wrong numbers!")

pythagoras_Theorem([3, 4, 5])
     