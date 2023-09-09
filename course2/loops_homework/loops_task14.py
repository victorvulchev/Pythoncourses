numb = int(input("Guess the number between 1 and 100:"))
import random
random_number = random.randint(1, 100)
while numb != random_number:
    if numb > random_number:
        print("Too high.")
    else:
        print("Too low.")
    numb = int(input())
print("Exactly right!")

