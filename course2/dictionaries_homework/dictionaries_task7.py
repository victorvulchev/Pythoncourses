import random
roll_times = 1000
two_counter = 0
three_counter = 0
four_counter = 0
five_counter = 0
six_counter = 0
seven_counter = 0
eight_counter = 0
nine_counter = 0
ten_counter = 0
eleven_counter = 0
twelve_counter = 0
for i in range(roll_times):
    numb = random.randint(2, 12)
    if numb == 2:
        two_counter += 1 
    elif numb == 3:
        three_counter += 1
    elif numb == 4:
        four_counter += 1
    elif numb == 5:
        five_counter += 1
    elif numb == 6:
        six_counter += 1
    elif numb == 7:
        seven_counter += 1
    elif numb == 8:
        eight_counter += 1
    elif numb == 9:
        nine_counter += 1
    elif numb == 10:
        ten_counter += 1
    elif numb == 11:
        eleven_counter += 1
    elif numb == 12:
        twelve_counter += 1

perc_2 = two_counter * 100 / roll_times
perc_3 = three_counter * 100 / roll_times
perc_4 = four_counter * 100 / roll_times
perc_5 = five_counter * 100 / roll_times
perc_6 = six_counter * 100 / roll_times
perc_7 = seven_counter * 100 / roll_times
perc_8 = eight_counter * 100 / roll_times
perc_9 = nine_counter * 100 / roll_times
perc_10 = ten_counter * 100 / roll_times
perc_11 = eleven_counter * 100 / roll_times
perc_12 = twelve_counter * 100 / roll_times

dict_1 = {2: 2.78,
          3: 5.56,
          4: 8.33,
          5: 11.11,
          6: 13.89,
          7: 16.67,
          8: 13.89,
          9: 11.11,
          10: 8.33,
          11: 5.56,
          12: 2.78}
dict_2 = {2: perc_2,
          3: perc_3,
          4: perc_4,
          5: perc_5,
          6: perc_6,
          7: perc_7,
          8: perc_8,
          9: perc_9,
          10: perc_10,
          11: perc_11,
          12: perc_12}
for i, g in dict_1.items():
    print(f"{i} : {g:.2f}")
for i, g in dict_2.items():
    print(f"{i} : {g:.2f}")