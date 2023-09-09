a = float(input("Price for paper:"))
b = float(input("Price for 20 words:"))
words = float(input("Number of words:"))
c = float(input("Price for every word after the first 20:"))
#text = input("Your text:")
#words = text.split()
#numb_Of_Words = len(words)

if words > 20:
    additional_cost = (words - 20) * c
    print(a + b + additional_cost)
else:
    print(a + b)