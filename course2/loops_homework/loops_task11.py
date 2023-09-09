for i in range(1,51,1):
    for j in range(1,51,1):
        for n in range(1,51,1):
            if i**2 + j**2 == n**3:
                print(f"Found result: {i}^2 + {j}^2 = {n}^3")