word = input()
word_to_use = word.lower()
letter_counter = 0
space_counter = 0
symbol_counter = 0
final_counter = 0
repetition = ""

for i in word_to_use:
    if i.isalpha():
        letter_counter += 1
    elif i.isspace():
        space_counter += 1
    else:
        symbol_counter += 1

    if i not in repetition:
        repetition += i

if repetition == word_to_use:
    print(0)
else:
    if letter_counter > 0:
        final_counter += 1
    if space_counter > 0:
        final_counter += 1
    if symbol_counter > 0:
        final_counter += 1
    print(final_counter)
